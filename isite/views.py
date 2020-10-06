from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import View, CreateView, ListView

from .models import Post, Page
from .forms import PostForm


class ViewMixin(View):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = Page.objects.filter(parent__isnull=True)
        context['fresh_posts'] = Post.objects.all()[:5]
        return context

class index(ViewMixin, ListView):
    model = Post
    paginate_by = 5
    template_name = 'index.html'


class PostDetailView(ViewMixin, DetailView):
    model = Post


class PageDetailView(ViewMixin, DetailView):
    model = Page


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_new.html'
    success_url = 'isite:post_detail.html'
