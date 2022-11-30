#!/bin/bash

set -e

if (($# < 1))
then
    echo "Image tag is not provided"
    echo "usage: ./tag_api_image.sh image_tag"
else
    TAG=$1
    docker context use default
    docker image build -t novahack_api:$TAG -f docker/api.dockerfile .
    docker tag novahack_api:$TAG 074132072645.dkr.ecr.eu-central-1.amazonaws.com/novahack_api:$TAG
    docker login -u AWS -p $(aws ecr get-login-password --region eu-central-1 --profile novahack) 074132072645.dkr.ecr.eu-central-1.amazonaws.com
    docker push 074132072645.dkr.ecr.eu-central-1.amazonaws.com/novahack_api:$TAG
    echo "Image created: 074132072645.dkr.ecr.eu-central-1.amazonaws.com/novahack_api:$TAG"
fi
