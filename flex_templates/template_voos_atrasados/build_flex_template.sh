gcloud dataflow $REPOS_NAME build gs://$BUCKET_NAME/templates/$IMAGE_NAME.json \
    --image-gcr-path "$REGION-docker.pkg.dev/$PROJECT_ID/$REPOS_NAME/$IMAGE_NAME:latest" \
    --sdk-language "PYTHON" \
    --flex-template-base-image "PYTHON3" \
    --metadata-file "metadata.json" \
    --py-path "." \
    --env "FLEX_TEMPLATE_PYTHON_PY_FILE=pipe_voos_to_bigquery.py" \
    --env "FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE=requirements.txt"