from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from rest_framework import viewsets

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# this means that queryset will query all the Book instances,meaning the view will handle operations on 
# all books in the database.
# serializer_class will use the BookSerializer to convert the Book model instances to JSON format
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()     # this is will fetch or retrieve all the book objects
    serializer_class = BookSerializer # this is will format the data of the BookSerializer
