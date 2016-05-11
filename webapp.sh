#!/bin/bash
cd /webapp/
source venv/bin/activate
sudo apt-get install python-pip -y
sudo pip install django
cd puppetenc
python manage.py runserver 0.0.0.0:8000 &
