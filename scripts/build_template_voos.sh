#!/bin/bash

# Preparação do template
python $TEMPLATE_MODULE \
    --project_id $PROJECT_ID \
	--table_name $TABLE_NAME \
	--dataset_name $DATASET_NAME \
	--bucket_name $BUCKET_NAME \
	--data_source $DATA_SOURCE \
	--runner $RUNNER \
	--project $PROJECT_ID \
	--staging_location "gs://${BUCKET_NAME}/staging" \
	--template_location "gs://${BUCKET_NAME}/templates/${TEMPLATE_NAME}" \
	--region $REGION \
	--save_main_session