#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# 👇 ADD THIS LINE (Replace 'backend' with your actual folder name if different)
cd backend 

python manage.py collectstatic --no-input
python manage.py migrate