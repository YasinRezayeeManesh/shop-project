# Generated by Django 5.1.1 on 2024-09-29 18:49

import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('image', models.ImageField(upload_to='images/articles', verbose_name='تصویر مقاله')),
                ('short_description', models.TextField(verbose_name='توضیحات کوتاه')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('description2', models.TextField(blank=True, null=True, verbose_name='توضیحات 2')),
                ('slug', models.SlugField(blank=True, default='', max_length=200, null=True, unique=True, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیرفعال')),
                ('shamsi_date', django_jalali.db.models.jDateField(auto_now_add=True, verbose_name='تاریخ شمسی')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
            },
        ),
    ]
