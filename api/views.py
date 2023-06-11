from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from api.serializer import ViewPostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from myapp.models import Post

class IsAuthorFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own posts.
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(author=request.user)


class ViewPostViewSet(ModelViewSet):
    serializer_class = ViewPostSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get', ]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
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


class UserPostsViewSet(ModelViewSet):
    serializer_class = ViewPostSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', ]

    filter_backends = [
        IsAuthorFilterBackend,
    ]

    def get_queryset(self):
        return Post.objects.all()