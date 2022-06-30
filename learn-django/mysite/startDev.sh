#!/bin/bash
python manage.py runserver

# Run a particular port instead of (8000)
# python manage.py runserver 8080

# For example, to listen on all available public IPs (which is useful if you are running Vagrant or want to show off your work on other computers on the network), use:
# python manage.py runserver 0:8000
# 0 is a shortcut for 0.0.0.0. 