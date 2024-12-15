from django.db import models

# Create your models here.

class Author(models.Model):
    """""
    This is the Author model store information about book authors.
    
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    """""
    This is the Book model information about books, including a reference to the author. 
    
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title