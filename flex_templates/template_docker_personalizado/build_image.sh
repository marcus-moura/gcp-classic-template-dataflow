
#!/bin/bash
gcloud builds submit --tag $REGION-docker.pkg.dev/$PROJECT_ID/$REPOS_NAME/dataflow/$IMAGE_NAME:$TAG

#   docker build -f Dockerfile -t $IMAGE_URI ./
#   docker push $IMAGE_URI