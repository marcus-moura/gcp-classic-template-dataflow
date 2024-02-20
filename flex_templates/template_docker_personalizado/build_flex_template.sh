gcloud dataflow $REPOS_NAME build gs://$BUCKET_NAME/templates/flow_voos_to_bigquery.json \
    --image "$REGION-docker.pkg.dev/$PROJECT_ID/$REPOS_NAME/dataflow/$IMAGE_NAME:$TAG" \
    --metadata-file "metadata.json" \
    --sdk-language PYTHON