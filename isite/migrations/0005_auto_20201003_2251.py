# Generated by Django 3.1.2 on 2020-10-03 19:51

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('isite', '0004_auto_20201003_1918'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Рубрика', 'verbose_name_plural': 'Рубрики'},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'Страница', 'verbose_name_plural': 'Страницы'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published_at'], 'verbose_name': 'Запись', 'verbose_name_plural': 'Записи'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=tinymce.models.HTMLField(verbose_name='Текст'),
        ),
    ]
