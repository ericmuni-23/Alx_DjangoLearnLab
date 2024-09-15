from django.contrib import admin
from .models import Book
from .models import CustomUser
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
from .models import MyModel
from django.contrib.auth.models import Group, Permission

group, created = Group.objects.get_or_create(name='Editors')
group.permissions.add(Permission.objects.get(codename='can_edit'))
group.permissions.add(Permission.objects.get(codename='can_create'))

group, created = Group.objects.get_or_create(name='Viewers')
group.permissions.add(Permission.objects.get(codename='can_view'))

group, created = Group.objects.get_or_create(name='Admins')
group.permissions.add(Permission.objects.get(codename='can_edit'))
group.permissions.add(Permission.objects.get(codename='can_create'))
group.permissions.add(Permission.objects.get(codename='can_delete'))

class MyModelGroup(GroupAdmin):
    model = Group
    list_display = ('name', 'permissions')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['permissions'].queryset = Permission.objects.filter(content_type__model='mymodel')
        return form

admin.site.register(Group, MyModelGroup)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'profile_photo')

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author')
    list_filter = ('title', 'author')


admin.site.register(Book, BookAdmin)
