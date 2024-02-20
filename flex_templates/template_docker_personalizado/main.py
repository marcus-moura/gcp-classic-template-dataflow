import apache_beam as beam
import os
from apache_beam.options.pipeline_options import PipelineOptions
from argparse import ArgumentParser

class Filtro(beam.DoFn):
    def process(self, record):
        if int(record[8]) > 0:
            return [record]

def criar_dict_nivel1(record):
    dict_ = {} 
    dict_['airport'] = record[0]
    dict_['lista'] = record[1]
    return dict_

def desaninhar_dict(record):
    def expand(key, value):
        if isinstance(value, dict):
            return [(key + '_' + k, v) for k, v in desaninhar_dict(value).items()]
        else:
            return [(key, value)]
    items = [item for k, v in record.items() for item in expand(k, v)]
    return dict(items)

def criar_dict_nivel0(record):
    dict_ = {} 
    dict_['airport'] = record['airport']
    dict_['lista_Qtd_Atrasos'] = record['lista_Qtd_Atrasos'][0]
    dict_['lista_Tempo_Atrasos'] = record['lista_Tempo_Atrasos'][0]
    return dict_
  
def run() -> None:

    class MyOptions(PipelineOptions):
        @classmethod
        def _add_argparse_args(cls, parser):
            parser.add_argument('--project_id', required=True, help="Id do projeto")
            parser.add_argument('--table_name', required=True, help="Nome da tabela")
            parser.add_argument('--dataset_name', required=True, help="Nome do dataset_name")
            parser.add_argument('--data_source', required=True, help="Fonte de dados")
            parser.add_argument('--bucket_name', required=True, help="Bucket para o armazenamento dos arquivos")

    options = MyOptions(save_main_session=True)

    table_schema = 'airport:STRING, lista_Qtd_Atrasos:INTEGER, lista_Tempo_Atrasos:INTEGER'
    abs_path_table = f"{options.project_id}:{options.dataset_name}.{options.table_name}"
    path_data_source = f"gs://{options.bucket_name}/input/{options.data_source}"
    
    with beam.Pipeline(options=options) as pipeline:
        Tempo_Atrasos = (
        pipeline  
            | "Importar Dados Atraso" >> beam.io.ReadFromText(path_data_source, skip_header_lines=1)
            | "Separar por Vírgulas Atraso" >> beam.Map(lambda record: record.split(','))
            | "Pegar voos com atraso" >> beam.ParDo(Filtro())
            | "Criar par atraso" >> beam.Map(lambda record: (record[4], int(record[8])))
            | "Somar por key" >> beam.CombinePerKey(sum)
        )

        Qtd_Atrasos = (
        pipeline
            | "Importar Dados" >> beam.io.ReadFromText(path_data_source, skip_header_lines=1)
            | "Separar por Vírgulas Qtd" >> beam.Map(lambda record: record.split(','))
            | "Pegar voos com Qtd" >> beam.ParDo(Filtro())
            | "Criar par Qtd" >> beam.Map(lambda record: (record[4], int(record[8])))
            | "Contar por key" >> beam.combiners.Count.PerKey()
        )

        tabela_atrasos = (
            {'Qtd_Atrasos': Qtd_Atrasos, 'Tempo_Atrasos': Tempo_Atrasos}
            | beam.CoGroupByKey()
            | beam.Map(lambda record: criar_dict_nivel1(record))
            | beam.Map(lambda record: desaninhar_dict(record))
            | beam.Map(lambda record: criar_dict_nivel0(record)) 
            | beam.io.WriteToBigQuery(
                abs_path_table,
                schema=table_schema,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                custom_gcs_temp_location=f"gs://{options.bucket_name}/temp"
            )
        )
  
if __name__ == '__main__':
    run()