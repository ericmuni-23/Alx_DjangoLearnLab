from django.db import models

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

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    