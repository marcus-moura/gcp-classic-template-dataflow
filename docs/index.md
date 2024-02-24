# GCP Classic Template
## Descrição
Este projeto facilita a construção de templates clássicos para fluxos de dados no Google Cloud Dataflow. Ele oferece uma estrutura robusta e flexível para criar pipelines de processamento de dados de forma eficiente e escalável. Além disso, inclui um pipeline de Integração Contínua/Entrega Contínua (CI/CD) simples para automatizar o processo de build e deploy.

## Estrutura do Projeto

```bash
├── .github/workflows
│   ├── pipeline-template-dataflow.yml
├── classic_template
│   ├── .env
│   ├── metadata.json
│   ├── pipe_voos_to_bigquery.py
├── input
│   ├── voos_sample.csv
├── setup_env
│   ├── build_template.sh
│   ├── create_bucket.sh
│   ├── deploy_job.sh
├── .gitignore
├── .python-version
├── poetry.lock
├── pyproject.toml
```


## Requisitos

Certifique-se de ter os seguintes pré-requisitos instalados:

- [Google Cloud SDK](https://cloud.google.com/sdk)
- [Python](https://www.python.org/)
- [Poetry](https://python-poetry.org/)

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/yourusername/cp-classic-template-dataflow.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd gcp-classic-template-dataflow
    ```

3. Instale as dependências usando poetry:
   
    ```bash
    poetry install
    ```
4. Ative o ambiente virtual do projeto:

    ```bash
    poetry shell
    ```

Dessa forma, você terá um ambiente Python isolado para o projeto, evitando conflitos entre dependências de outros projetos.

## Uso

### Carregando Variáveis de Ambiente
Comece carregando as variáveis de ambiente definidas em seu arquivo `.env` com o seguinte comando:
```bash
export $(cat classic_template/.env | xargs)
```

!!! tip "Dica"
    Utilize o arquivo classic_template/exemplo.env como base.

### Configuração do Bucket

Para criar o bucket, execute o seguinte script:
```bash title="create_bucket.sh"
gcloud storage buckets create gs://$BUCKET_NAME --default-storage-class STANDARD --location $REGION
```
!!! note "Nota"
    Dentro do bucket, crie um diretório chamado `input` e faça o upload do  arquivo `input/sample.csv`.

### Construção do Template
Prepare o template executando o script `build_template.sh` na pasta `setup_env`:
```bash title="build_template.sh"
sh setup_env/build_template.sh
```

### Implantação
Para criar um job com base no template, execute o seguinte comando:
```bash 
sh setup_env/deploy_job.sh
```

### Configuração do CI/CD
Configure os jobs de CI/CD no GitHub Actions, seguindo o exemplo do arquivo `pipeline-template-dataflow.yml`.

### Fluxo do CI/CD

O pipeline de CI/CD é acionado por pushs na branch `main` e executa as seguintes etapas:
- Instalação do Poetry.
- Autenticação no Google Cloud.
- Configuração do SDK do Google Cloud.
- Construção do template para o bucket.
- Implantação do template no Dataflow.

## Links Úteis

- [Documentação do Google Cloud SDK](https://cloud.google.com/sdk)
- [Python](https://www.python.org/)
- [GitHub Actions](https://docs.github.com/pt/actions)