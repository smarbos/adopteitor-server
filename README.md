# adopteitor

### Instalacion

#### Server:

Create Virtual Environment:

    mkvirtualenv venv

Select Virtual Environment to work on:

    workon venv

Install dependencies:

    pip install -r requirements.txt

Run Migrate:

    python manage.py migrate

Create superuser to access backend:

    python manage.py createsuperuser

Run server:

    python manage.py runserver

### Usage

Run client:
    cd client && npm start

Run server:
    cd server && workon venv && python manage.py runserver

Run gulp:
    cd client && gulp && gulp watch


### Create fixtures
  python manage.py dumpdata adopteitor_core.Animal adopteitor_core.AnimalFoto --output fixtures.json --indent 2

### Load fixtures
   python manage.py loaddata fixtures.json
