from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='Категория')
    slug = models.SlugField(allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рубрика"
        verbose_name_plural = "Рубрики"


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    category = models.ForeignKey(
        Category,
        related_name='posts',
        on_delete=models.CASCADE,
        verbose_name='Рубрика')
    published_at = models.DateField(
        auto_now=False,
        auto_now_add=False,
        verbose_name='Дата публикации')
    text = HTMLField(verbose_name='Текст')
    author = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE,
        verbose_name="Автор")
    slug = models.SlugField(allow_unicode=True)

    def __str__(self):
        return self.title

    def get_previous_post(self):
        return Post.objects.get(id = self.id-1)


    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ['-published_at']


class Page(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = HTMLField(verbose_name="Текст")
    parent = models.ForeignKey(
        "self",
        related_name='parents',
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    slug = models.SlugField(allow_unicode=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"
