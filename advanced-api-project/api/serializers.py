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

