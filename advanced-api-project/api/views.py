"from django_filters import rest_framework"
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
"from rest_framework.filters import OrderingFilter"
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framwork.views import APIView
from rest_framework.response import Response
from .models import Author
from .serializers import AuthorSerializer
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter
# Create your views here.
# List all the books
class BookListView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ["title", "author", "publication_year"]
    ordering_fields = ["title", "publication_year"]
    ordering = ["title"]  # Default ordering

class BookListView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ["title", "author", "publication_year"]
    search_fields = ["title", "author"]  # Fields that can be searched
    ordering_fields = ["title", "publication_year"]
    ordering = ["title"]  # Default ordering

class AuthorListView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    
# this to list all the books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # this is allow the public access for listing books

# this is to retrieve a single book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Allow unauthenticated users to view


# thi is to create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can create books
    

# Update a new book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Only authenticated user can update books


# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Only authenticated for users to can delete 

