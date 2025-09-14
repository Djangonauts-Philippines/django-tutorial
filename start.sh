#!/bin/bash

echo "Starting Django server..."
gunicorn -b 0.0.0.0 -p $PORT djangotutorial.wsgi:application