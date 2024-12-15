from django.shortcuts import render
from rest_framework import APIView
from .models import Author
from .models import authors
from .models import Response
from .serializers import AuthorSerializer

# Create your views here.

class AuthorListView(APIView):
    def get(self, request):
        author = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)