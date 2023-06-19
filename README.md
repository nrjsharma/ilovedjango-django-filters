# Filters in Django Rest Framework

<p align="center">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="ilovedjango.png">
      <source media="(prefers-color-scheme: light)" srcset="ilovedjango.png">
      <img alt="Filters in Django Rest Framework" width="350px" title="Filters in Django Rest Framework" src="ilovedjango.png">
    </picture>
</p>


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

### Run

```shell
# run migrations
python manage.py migrate
# run server
python manage.py runserver 0:8000
```
# Overview

Django REST Framework list view by default returns entire query sets for the model. We use filters provided by Django to filter out the queryset.

- DjangoFilterBackend
- SearchFilter
- OrderingFilter

## Installation
To configure Django filters in your Django project, you need to install `django-filter` packages
```shell
pip install django-filter
```
And then define the django filters in ``INSTALLED_APPS`` in ``settings.py`` file

```python
INSTALLED_APPS = [
    ...
    # Django REST framework
    'rest_framework',
    # Django Filters
    'django_filters',
]
```
You can set the default filter backend in ``settings.py`` file. Then these filters are set globally for all the View or ViewSet.
```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
}
```
You can also set the filter backend to an individual View or ViewSet.
```python
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class MyModelViewSet(ModelViewSet):

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
```
# DjangoFilterBackend
The `DjangoFilterBackend` class is used to filter the queryset according to a specified set of fields. By automatically generating a FilterSet class for the specified field.
```python
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from api.serializer import ViewPostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from myapp.models import Post


class ViewPostViewSet(ModelViewSet):
    serializer_class = ViewPostSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get', ]

    filter_backends = [
        DjangoFilterBackend,
    ]

    filterset_fields = {
        "title": ["icontains", "startswith"],
        "author__email": ["icontains", ],  # ForeignKey
        "is_active": ["exact", ],  # BooleanField
        "created_at": ["date__exact", ]  # DateTimeField
    }

    def get_queryset(self):
        return Post.objects.all()
```

# SearchFilter

The `SearchFilter` class supports simple single query parameter-based searching

```python
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from api.serializer import ViewPostSerializer
from myapp.models import Post
from rest_framework import filters


class ViewPostViewSet(ModelViewSet):
    serializer_class = ViewPostSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get', ]

    filter_backends = [
        filters.SearchFilter,
    ]

    # Search Behavior
    # '^' Starts with search.
    # '=' Exact matches search.
    # '@' Full-text search. (Supported only in Django's PostgreSQL backend.)
    # '$' Regex search.

    search_fields = ['^title', '=author__email']

    def get_queryset(self):
        return Post.objects.all()
```
# OrderingFilter
The `OrderingFilter` class allows you to order the queryset result according to a specified set of fields.
```python
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from api.serializer import ViewPostSerializer
from myapp.models import Post
from rest_framework import filters


class ViewPostViewSet(ModelViewSet):
    serializer_class = ViewPostSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get', ]

    filter_backends = [
        filters.OrderingFilter,
    ]

    ordering_fields = ['id', 'author_id']

    # Default ordering
    ordering = ['-id']

    def get_queryset(self):
        return Post.objects.all()
```
Learn [more](https://ilovedjango.com/django/rest-api-framework/filters-in-django-rest-framework/) about Filter in Django Rest Framework
