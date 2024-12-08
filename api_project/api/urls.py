from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

# create the router and register our BookViewSets with it
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename = 'books_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
    path('api-token-auth/', name = 'obtain_auth_token'),
]

# DefaultRouter: this will router automatically generates the necessary URL patterns for all CRUD operations
# (list, create, retrieve, update, delete)

#router.register(): this register BookViewSet with the router and maps it to the books_all URL path.
#basename argument is used to name the viewset for URL generation