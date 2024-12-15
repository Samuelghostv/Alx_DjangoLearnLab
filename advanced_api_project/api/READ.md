from django.db import models
## models.py file
# Create your models here.

class Author(models.Model):
    """" 
    This is the Author model that will store the information about the authors
    """
    name =models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """""
    This is the Book model the will store information about the books, including a reference to the author.
    - title: the title of the book (string).
    - publication_year: the year of the book was published (integer)
    - author: A foreign key relationship linking each book to an author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

## serializers.py file

# create serializer

from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """""
    The serializer for the Book model, includes custom validation for publication_year.
    """
    class Meta:
        model = Book
        fields =["title", "publication_year", "author"]

    def validate_publication_year(self, value):
        """""
        Custom validation for publication_year is not in the future.
        """
        from datetime import datetime
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value
    
class AuthorSerializer(serializers.ModelSerializer):
    """""
    Serializer for the Author model. Includes a nested BookSerializer to represent related books.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["name", "books"]