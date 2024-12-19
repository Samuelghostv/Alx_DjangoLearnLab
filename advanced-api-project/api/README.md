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
