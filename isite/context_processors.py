from .models import Page, Post


def extras(request):
    pages = Page.objects.filter(parent__isnull=True)
    fresh_posts = Post.objects.all()[:5]
    return {'pages': pages, 'fresh_posts': fresh_posts}