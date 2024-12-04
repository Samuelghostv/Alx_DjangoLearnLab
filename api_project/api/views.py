from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()     # this is will fetch or retrieve all the book objects
    serializer_class = BookSerializer # this is will format the data of the BookSerializer
