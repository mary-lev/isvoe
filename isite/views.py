from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Post

def index(request):
    text = "Свое издательство"
    posts = Post.objects.all()
    return render(request, 'isite/index.html', {'text': text, 'posts': posts})


class PostDetailView(DetailView):
    model = Post
