from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Author(models.Model):
   # Stores the name of the author
   name = models.CharField(max_length=100)

class Book(models.Model):
   # Stores the book title, publication year, and links to an author
   title = models.CharField(max_length=200)
   publication_year = models.IntegerField()
   author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
