web: gunicorn core.wsgi:application --log-file -
python manage.py collectstatic --noinput
manage.py migrate