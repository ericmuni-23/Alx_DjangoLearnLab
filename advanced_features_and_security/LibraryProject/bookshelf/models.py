from django.db import models
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    class Meta:
        permissions = [
            ('can_view', 'Can view documents'),
            ('can_create', 'Can create documents'),
            ('can_edit', 'Can edit documents'),
            ('can_delete', 'Can delete documents'),
        ]

    def __str__(self):
        return self.title

class Author(models.Model):
    name=models.CharField(max_length=215)

    def __str___(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=215)
    author =models.ForeignKey (Author ,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Library(models.Model):
        name = models.CharField(max_length=215)
        books =models.ManyToManyField(Book)

        def __str__(self):
            return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=215)
    library = models.OneToOneField(Library,on_delete=models.CASCADE)

    def __str__(self):
            return self.name

