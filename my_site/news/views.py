from django.shortcuts import render
from .models import *


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
     }
    return render(request, 'news/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'title': 'Список новостей',
        'category': category,
    }
    return render(request, 'news/category.html', context)
