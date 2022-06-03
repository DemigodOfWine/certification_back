command = '/home/jj/www/certification_django/env/bin/gunicorn'
pythonpath = '//home/jj/www/certification_django/certification'
bind = '127.0.0.1:8000'
workers = 5
user = 'jj'
limit_request_fields = 32000
limit_request_field_size = 0

raw_env = 'DJANGO_SETTINGS_MODULE=certification.settings'
