from django.contrib import admin
from .models import Author, Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .import admin_site, CustomUserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm 



# Integrate the user admin with our user model
class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display =["username", "email", "date_of_birth", "profile_photo", "is_admin"]

    admin_site.register(CustomUser, CustomUserAdmin)

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
