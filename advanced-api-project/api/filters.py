import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains", label="Title (contains)")
    author = django_filters.CharFilter(lookup_expr="icontains", label="Author (contains)")
    publication_year = django_filters.NumberFilter(field_name="publication_year", lookup_expr='exact')

    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]
