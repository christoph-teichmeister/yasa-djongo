#!/usr/bin/env bash

echo "" && echo "Running migrations" && echo ""
python ./manage.py migrate

echo "" && echo "Starting Development server" && echo ""
python ./manage.py runserver 0.0.0.0:8000