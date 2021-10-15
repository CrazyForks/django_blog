# Generated by Django 3.2.5 on 2021-10-15 07:33

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20211015_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='article_count',
            field=models.IntegerField(default=0, help_text='该分类下，有多少篇文章', verbose_name='文章数'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default=blog.models.category_haveNo, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='articles', to='blog.category', verbose_name='文章分类'),
        ),
    ]