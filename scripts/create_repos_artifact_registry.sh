#!/bin/bash

gcloud artifacts repositories create $REPOS_NAME \
    --repository-format=$REPOSITORY_FORMAT \
    --location=$REGION