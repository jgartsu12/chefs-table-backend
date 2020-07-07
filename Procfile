web: gunicorn chefsBackEnd.wsgi:application --log-file=-

web: gunicorn chefsBackEnd.wsgi --log-level=info --log-file - --log-level debug
python manage.py collectstatic --noinput

gunicorn chefsBackEnd.wsgi:application --preload --workers 1


