from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *


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


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News,pk=news_id)
    context = {
        'news_item': news_item,
    }
    return render(request, 'news/view_news.html', context)


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})
