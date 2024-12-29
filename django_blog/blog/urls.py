
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path("", PostListView.as_view(), name= "post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name= "post_detail"),
    path("post/new/", PostCreateView.as_view(), name= "post_create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name= "post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name= "post_delete"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
]
