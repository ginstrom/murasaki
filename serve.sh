#!/bin/zsh
# collect and compile messages
python3 manage.py makemessages -l ja --settings=murasaki.settings.dev
python3 manage.py compilemessages --settings=murasaki.settings.dev
# Serve the site locally
python3 manage.py runserver --settings=murasaki.settings.dev
