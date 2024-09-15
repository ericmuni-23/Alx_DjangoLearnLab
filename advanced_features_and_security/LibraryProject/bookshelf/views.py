from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article

@permission_required('app_name.can_view', raise_exception=True)
def view_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'view_article.html', {'article': article})

@permission_required('app_name.can_create', raise_exception=True)
def create_article(request):
    # Implementation for creating an article
    pass

@permission_required('app_name.can_edit', raise_exception=True)
def edit_article(request, article_id):
    # Implementation for editing an article
    pass

@permission_required('app_name.can_delete', raise_exception=True)
def delete_article(request, article_id):
    # Implementation for deleting an article
    pass
