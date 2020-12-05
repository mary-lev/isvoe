from django.contrib.auth.models import User
from django.db import models


class Letter(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateField(blank=True, auto_now=False, auto_now_add=False, verbose_name='Дата публикации')


class Page(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    slug = models.SlugField(allow_unicode=True)


    def __str__(self):
        return self.title