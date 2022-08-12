from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import *
from .forms import *


class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'  #по дефолту news_list.html
    context_object_name = 'news'  #по дефолту object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)    #чтобы отображались только опубликованные


class NewsByCategory(ListView):
    model = News
    template_name = 'news/index.html'  # сделаем что шаблон одинаковай
    context_object_name = 'news'  # по дефолту object_list
    allow_empty = False    #чтоб на несуществующих страницах показывало 404 вместо 500 ошибки

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)



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
