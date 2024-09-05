from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Book
from .models import Library
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


def list_books(request):
    books = Book.objects.all()
    return render (request, 'relationship_app/list_books.html',{'books':books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home or any page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=['Admin', 'Librarian', 'Member'])

    def __str__(self):
        return self.user.username
    #reciever(post_save,sender=User)   
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objectscreate(user=instance)

def admin_view(request):
    if request.user.userprofile.role == 'Admin':
        return render(request, 'admin.html')
    else:
        return render(request, 'access_denied.html')

def librarian_view(request):
    if request.user.userprofile.role == 'Librarian':
        return render(request, 'librarian.html')
    else:
        return render(request, 'access_denied.html')

def member_view(request):
    if request.user.userprofile.role == 'Member':
        return render(request, 'member.html')
    else:
        return render(request, 'access_denied.html')
    

