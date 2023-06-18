# Filters in Django Rest Framework

### Install

```shell
# clone project
git clone git@github.com:nrjsharma/ilovedjango-django-filters.git
# create env
pyenv virtualenv 3.8.0 djangofilters
# enable env
pyenv activate djangofilters
# install requirements
pip install -r requirements.txt
```

### Run Locally

```shell
# run migrations
python manage.py migrate
# run server
python manage.py runserver 0:8000
```
# Filters

Django REST Framework list view by default returns entire query sets for the model. We use filters provided by Django to filter out the queryset.

- DjangoFilterBackend
- SearchFilter
- OrderingFilter

