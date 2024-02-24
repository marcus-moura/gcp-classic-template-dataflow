#!/bin/bash

poetry run gcloud dataflow jobs run $JOB_NAME \
            --gcs-location gs://${BUCKET_NAME}/templates/${TEMPLATE_NAME} \
            --parameters table_name=$TABLE_NAME \
            --region $REGION