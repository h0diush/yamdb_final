python3 manage.py makemigrations

python3 manage.py migrate --noinput

python3 manage.py collectstatic --noinput

gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000