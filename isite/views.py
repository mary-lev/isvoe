from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Post, Page

def index(request):
    text = "Свое издательство"
    posts = Post.objects.all()
    pages = Page.objects.filter(parent__isnull=True)
    return render(request, 'isite/index.html', {'text': text, 'posts': posts, 'pages': pages})


class PostDetailView(DetailView):
    model = Post


class PageDetailView(DetailView):
    model = Page