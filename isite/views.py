from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic import View, CreateView, ListView

from .models import Post, Page
from .forms import PostForm


class IndexView(ListView):
    """
    Главная страница сайта: вывод пяти последних постов.
    """
    model = Post
    paginate_by = 5
    template_name = 'index.html'
    queryset = Post.objects.all()


class PostDetailView(DetailView):
    """
    Шаблон для одного поста.
    """
    model = Post


class PageDetailView(DetailView):
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
