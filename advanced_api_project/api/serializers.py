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