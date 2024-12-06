from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
# this will serializer all the fields of the book model
# BookSerializer users DRF ModelSerializer to automatically generate fields based on the Book model
# fields =' __all__' ensures all fields from the Book model are included in the API