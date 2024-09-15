from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.username

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

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username