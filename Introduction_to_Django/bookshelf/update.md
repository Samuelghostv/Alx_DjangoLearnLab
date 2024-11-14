```python
# Importing the Book model from the bookshelf app
>>> from bookshelf.models import Book

# Retrieving the book instance with the title "1984"
>>> new_book = Book.objects.get(title='1984')

# Checking the current details of the book
>>> new_book
    # Expected Output: Title: 1984, Author: George Orwell, Year: 1949

# Updating the title of the book to "Nineteen Eighty-Four" and saving changes
>>> new_book.title = "Nineteen Eighty-Four"
>>> new_book.save()

# Verifying the updated book details
>>> new_book
    # Expected Output: Title: Nineteen Eighty-Four, Author: George Orwell, Year: 1949

# Checking the title specifically to confirm the update
>>> new_book.title
    # Expected Output: 'Nineteen Eighty-Four'

# Checking that the Book model is also updated accordingly
>>> Book.objects.all()
    # Expected Output: <QuerySet [Title: Nineteen Eighty-Four, Author: George Orwell, Year: 1949]>