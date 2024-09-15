from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, date_of_birth, password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.username
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

