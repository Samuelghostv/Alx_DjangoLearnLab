from django.shortcuts import render
from rest_framwork.views import APIView
from rest_framework.response import Response
from .models import Author
from .serializers import AuthorSerializer
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.permissions import IsAdminOrReadOnly

# Create your views here.
# List all the books

class AuthorListView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    
# this to list all the books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny] # this is allow the public access for listing books

# this is to retrieve a single book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny] 

# thi is to create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can create books
    def perform_create(self, serializer):
        serializer.save() # Add custom behavior if necessary, e.g., log creation, etc.

# Update a new book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Only authenticated user can update books
    def perform_update(self, serializer): # Add custom update the logic here
        serializer.save() # Save the updated instance

# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Only authenticated for users to can delete 

from .permissions import IsAdminOrReadOnly

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]


