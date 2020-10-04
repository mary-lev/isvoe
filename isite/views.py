from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Post, Page

def index(request):
    text = "Свое издательство"
    posts = Post.objects.all()[:5]
    pages = Page.objects.filter(parent__isnull=True)
    return render(request, 'isite/index.html', {'text': text, 'fresh_posts': posts, 'pages': pages})


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = Page.objects.filter(parent__isnull=True)
        context['fresh_posts'] = Post.objects.all()[:5]
        return context


class PageDetailView(DetailView):
    model = Page

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = Page.objects.filter(parent__isnull=True)
        context['fresh_posts'] = Post.objects.all()[:5]
        return context
