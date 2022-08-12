from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
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


class VeiwNews(DetailView):
    model = News
    context_object_name = 'news_item'
    # pk_url_kwarg = 'news_id'
    template_name = 'news/view_news.html'  # по дефолту news_detail.html


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})
