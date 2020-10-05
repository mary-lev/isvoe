from django import forms

from .models import Post, Page, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'title', 'category']