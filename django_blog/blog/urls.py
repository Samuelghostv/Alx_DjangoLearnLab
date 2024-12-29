
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name= "post_list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name= "post_detail"),
    path("posts/new/", PostCreateView.as_view(), name= "post_create"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name= "post_edit"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name= "post_delete"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
]
