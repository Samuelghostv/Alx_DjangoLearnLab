```python
#Import the Book model
>>> from bookshelf.models import Book

#Create a Book instance with the title "1984", author "George Orwell", and publication year 1949.
>>> Book.objects.create(title='1984', author='George Orwell', publication_year=1949) 
    #Expected Output: Title: 1984, Author: George Orwell, Year: 1949

#Retrieve and display the attributes of the book created.
>>> Book.objects.get().title 
    #Expected Output: '1984'

>>> Book.objects.get().author
    #Expected Output: 'George Orwell'

>>> Book.objects.get().publication_year
    #Expected Output: 1949

#Update the title of "1984" to "Nineteen eighty-four"
>>> Book.objects.filter(title='1984').update(title='Nineteen eighty-four')
    #Expected Output: 1

#Confirm the update by retrieving the title
>>> Book.objects.get().title
    #Expected Output: 'Nineteen eighty-four'

#Delete the book with the updated title "Nineteen eighty-four"
>>> Book.objects.filter(title='Nineteen eighty-four').delete()
    #Expected Output: (1, {'bookshelf.Book': 1})

#Confirm deletion by retrieving all Book objects
>>> Book.objects.all()
    #Expected Output: <QuerySet []>
