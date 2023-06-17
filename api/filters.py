import django_filters
from myapp.models import Post


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='startswith')
    author = django_filters.NumberFilter(lookup_expr='id__exact')  # FK
    author__username = django_filters.AllValuesFilter(lookup_expr='exact')  # FK
    created_at = django_filters.DateFilter(lookup_expr='date__exact')  # date
    is_active = django_filters.BooleanFilter(lookup_expr='exact')  # boolean

    class Meta:
        model = Post
        fields = ['id', 'title']