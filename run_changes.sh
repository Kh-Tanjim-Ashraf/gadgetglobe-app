#!/bin/bash

# Migration Commands & Run the dev server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 8080