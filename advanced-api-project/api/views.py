from django.shortcuts import render
from rest_framwork.views import APIView
from rest_framework.response import Response
from .models import Author
from .serializers import AuthorSerializer

# Create your views here.

class AuthorListView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)