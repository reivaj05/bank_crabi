#!/bin/bash

python manage.py migrate
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin@crabi.com', 'admin@crabi.com', 'password')"
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin2@crabi.com', 'admin2@crabi.com', 'password')"
python manage.py runserver 0.0.0.0:8000