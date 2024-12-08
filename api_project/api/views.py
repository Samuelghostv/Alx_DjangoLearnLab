from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# to create IsAuthenticated permission class
class MyViewSet(APIView):
    permission_class = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You are authenticated User!"}, status=status.HTTP_200_OK)
#IsAuthenticated: ensures that only authenticated users can access the view


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
