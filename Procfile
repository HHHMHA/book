release: python manage.py migrate
web: gunicorn $PWD/book.wsgi:application