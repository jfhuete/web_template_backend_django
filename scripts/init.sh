#!/bin/bash

set -e

docker-compose up -d db

while netstat -lnt | awk '$4 ~ /:5432$/ {exit 1}'; do sleep 1; done

sleep 2

./scripts/manage.sh migrate
./scripts/manage.sh createsuperuser

docker-compose stop db

pre-commit install
