#!/bin/bash

docker-compose run --rm api python manage.py $@
