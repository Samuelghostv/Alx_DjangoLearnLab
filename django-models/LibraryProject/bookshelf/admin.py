from django.contrib import admin
from .models import Author, Book

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title","publication_year","author"]
    search_fields = ["title"]
    list_filter = ["publication_year"]
