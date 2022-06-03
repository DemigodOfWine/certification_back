#!/bin/bash
source /home/jj/www/certification_django/env/bin/activate
source /home/jj/www/certification_django/env/bin/postactivate
exec gunicorn  -c "/home/jj/www/certification_django/certification/certification/gunicorn_config.py" certification.wsgi