from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, book

class BookTests(APITestCase):

    def setUp(self):
        # Create a user to authenticate with
        self.user = User.objects.create_user(username='testuser', password='password')
        self.url = '/api/books/'  # Assuming your API endpoint for books is /api/books/
        self.data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'publication_year': 2020
        }

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.data['title'])
        self.assertEqual(response.data['author'], self.data['author'])
        self.assertEqual(response.data['publication_year'], self.data['publication_year'])

    def test_get_books(self): # Test Retrieve Book List (GET request):
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)  # At least one book should be returned

        def test_get_single_book(self):
        # First create a book
         book = Book.objects.create(title='Another Test Book', author='Another Author', publication_year=2021)
        response = self.client.get(f'/api/books/{book.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], book.title)

        def test_update_book(self):
         book = Book.objects.create(title='Test Book', author='Test Author', publication_year=2020)
        updated_data = {'title': 'Updated Test Book', 'author': 'Updated Author', 'publication_year': 2024}
        response = self.client.put(f'/api/books/{book.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], updated_data['title'])
        self.assertEqual(response.data['author'], updated_data['author'])

        def test_delete_book(self):
          book = Book.objects.create(title='Test Book', author='Test Author', publication_year=2020)
        response = self.client.delete(f'/api/books/{book.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Verify the book is deleted
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(id=book.id)

        def test_filter_by_author(self):
          Book.objects.create(title='Book 1', author='Author A', publication_year=2020)
        Book.objects.create(title='Book 2', author='Author B', publication_year=2021)
        response = self.client.get(self.url, {'author': 'Author A'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author A')

        def test_order_by_title(self):
         Book.objects.create(title='A Book', author='Author A', publication_year=2020)
        Book.objects.create(title='B Book', author='Author B', publication_year=2021)
        response = self.client.get(self.url, {'ordering': 'title'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'A Book')

        def test_create_book_unauthenticated(self):
           response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)






        
