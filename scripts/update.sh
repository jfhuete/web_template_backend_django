#!/bin/bash

set -e

docker-compose stop
git pull origin master
docker-compose up -d
