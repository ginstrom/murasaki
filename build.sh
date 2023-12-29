#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

export DJANGO_SETTINGS_MODULE=murasaki.settings.prod
python manage.py collectstatic --no-input
python manage.py migrate --settings=murasaki.settings.prod