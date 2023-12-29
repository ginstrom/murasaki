#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

DJANGO_SETTINGS_MODULE=murasaki.settings.dev manage.py collectstatic --no-input
python manage.py migrate --settings=murasaki.settings.prod