#!/usr/bin/env bash
set -o errexit  # stop the script if any command fails

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
