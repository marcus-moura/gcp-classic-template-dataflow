#!/bin/bash

gcloud storage buckets create gs://$BUCKET_NAME --default-storage-class STANDARD --location $REGION