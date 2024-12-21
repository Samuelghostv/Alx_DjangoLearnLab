from django.db import models

# Create your models here.

class Author(models.Model):
    """""
    This is the Author model store information about book authors.
    
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    """""
    This is the Book model information about books, including a reference to the author. 
    
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    - title: the title of the book (string)
    - publication_year: the year the book was published (integer)
    - author: A foreign key relationship linking each book to an author.

    def __str__(self):
        return self.title

from rest_framework import serializers
from .models import Author, Book

# creating custom serializers for our models

class BookSerializer(serializers.ModelSerializer):
    """"
    Serializer for the Book model. includes custom validation for publication_year.
    
    """
def validate_publication_year(self, value):
    """
    Custom validation to ensure that the publication year is not in the future.

    """
    from datetime import datetime
    current_year = datetime.now().year
    if value > current_year:
        raise serializers.ValidationError("The publication year cannot be in the future.")
    return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model. includes a nested BookSerializer to represent related books.

    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["name", "books"]

# Book API Documentation

This API allows for CRUD operations on books.

## Endpoints

### List Books
- `GET /books/`
- Retrieves a list of all books.
- Accessible to all users.

### Retrieve Book
- `GET /books/<id>/`
- Retrieves a single book by its ID.
- Accessible to all users.

### Create Book
- `POST /books/create/`
- Allows authenticated users to create a new book.

### Update Book
- `PUT /books/<id>/update/`
- Allows authenticated users to update a book by its ID.

### Delete Book
- `DELETE /books/<id>/delete/`
- Allows authenticated users to delete a book by its ID.

 Request Documentation:
Filter by title:

bash
Copy code
/api/books/?title=python
This returns all books with "python" in the title.

Search for books:

bash
Copy code
/api/books/?search=django
This searches for books with "django" in the title or author.

Order by publication year:

bash
Copy code
/api/books/?ordering=-publication_year

class BookListView(viewsets.ModelViewSet):
    """
    This view allows users to:
    - Filter books by title, author, or publication year
    - Search books by title or author
    - Order books by title or publication year

    Example requests:
    - Filter by title: `GET /books/?title=Harry Potter`
    - Search by author: `GET /books/?search=Rowling`
    - Order by publication year (ascending): `GET /books/?ordering=publication_year`
    - Order by title (descending): `GET /books/?ordering=-title`
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

## Testing

"""
Testing Strategy:

- Create a user, authenticate them, and test the CRUD operations for the `Book` model.
- Test the filtering functionality to ensure books can be filtered by title, author, and publication year.
- Test the search functionality to verify that books can be searched by title and author.
- Test ordering to ensure that books can be ordered by title and publication year.
- Test permissions to ensure unauthorized users cannot perform restricted operations.
- Test edge cases such as attempting to delete non-existing books or search with empty fields.

Run the tests using: `python manage.py test api`
"""
