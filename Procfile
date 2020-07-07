web: gunicorn chefsBackEnd.wsgi --log-level=info --log-file -
python manage.py collectstatic --noinput

gunicorn chefsBackEnd.wsgi:application --preload --workers 1


