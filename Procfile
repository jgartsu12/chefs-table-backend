web: gunicorn chefsBackEnd.wsgi --log-level=info --log-file -
python manage.py collectstatic --noinput

gunicorn project.wsgi:application --preload --workers 1


