#!bin/bash

poetry run python -m classic_template.pipe_voos_to_bigquery \
    --project_id $PROJECT_ID \
    --table_name $TABLE_NAME \
    --dataset_name $DATASET_NAME \
    --bucket_name $BUCKET_NAME \
    --data_source $DATA_SOURCE \
    --runner DataflowRunner \
    --project $PROJECT_ID \
    --staging_location "gs://${BUCKET_NAME}/staging" \
    --template_location "gs://${BUCKET_NAME}/templates/${TEMPLATE_NAME}" \
    --region $REGION \
    --save_main_session