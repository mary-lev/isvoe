from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import View, CreateView, ListView

from .models import Post, Page
from .forms import PostForm


class ViewMixin(View):
    """
    Основа для страниц сайта:
    передаются последние записи и страницы для навигации.
    """
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = Page.objects.filter(parent__isnull=True)
        context['fresh_posts'] = Post.objects.all()[:5]
        return context


class IndexView(ViewMixin, ListView):
    """
    Главная страница сайта: вывод пяти последних постов.
    """
    model = Post
    paginate_by = 5
    template_name = 'index.html'
    queryset = Post.objects.all()


class PostDetailView(ViewMixin, DetailView):
    """
    Шаблон для одного поста.
    """
    model = Post


class PageDetailView(ViewMixin, DetailView):
    """
    Шаблон для одной страницы.
    """
    model = Page


class PostCreateView(CreateView):
    """
    Форма для создания нового поста.
    """
    model = Post
    form_class = PostForm
    template_name = 'post_new.html'
    success_url = 'isite:post_detail.html'
