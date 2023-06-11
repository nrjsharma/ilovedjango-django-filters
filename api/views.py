from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from api.serializer import ViewPostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from myapp.models import Post


class ViewPostViewSet(ModelViewSet):
    serializer_class = ViewPostSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get', ]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    # DjangoFilterBackend
    filterset_fields = {
        "title": ["icontains", "startswith"],
        "author__email": ["icontains", ],  # ForeignKey
        "is_active": ["exact", ]  # BooleanField
    }

    # SearchFilter

    # Search Behavior
    # '^' Starts with search.
    # '=' Exact matches search.
    # '@' Full-text search. (Supported only in Django's PostgreSQL backend.)
    # '$' Regex search.

    search_fields = ['^title', '=author__email']

    # OrderingFilter
    ordering_fields = ['id', 'author_id']

    # Default ordering
    ordering = ['-id']

    def get_queryset(self):
        return Post.objects.all()