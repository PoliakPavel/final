from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .utils import Mymixin
from .models import *
from .forms import *


class HomeNews(Mymixin, ListView):
    model = News
    template_name = 'news/index.html'  #по дефолту news_list.html
    context_object_name = 'news'  #по дефолту object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(Mymixin, ListView):
    model = News
    template_name = 'news/index.html'  # сделаем что шаблон одинаковай
    context_object_name = 'news'  # по дефолту object_list
    allow_empty = False    #чтоб на несуществующих страницах показывало 404 вместо 500 ошибки

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class VeiwNews(DetailView):
    model = News
    context_object_name = 'news_item'
    # pk_url_kwarg = 'news_id'
    template_name = 'news/view_news.html'  # по дефолту news_detail.html


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'  # меняем на существующий шаблон
    # success_url = reverse_lazy('home')  типа если надо переопределить переход отличный от get_absolute_url

