#rest_boiler

# Prerequisites
- [Django 1.8.2]
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [postgresql](http://www.postgresql.org/)
- [heroku toolbelt](https://toolbelt.heroku.com/)

# Initialize the project
Create and activate a virtualenv:

```bash
virtualenv env
source env/bin/activate
```
Install dependencies:

```bash
pip install -r requirements/local.txt
```
Update the database settings:

Initialize the git repository

```
git init
git remote add origin https://github.com/erjaymodi/rest-boiler.git
```

Migrate, create a superuser, and run the server:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
