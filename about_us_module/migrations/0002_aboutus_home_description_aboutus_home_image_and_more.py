# Generated by Django 5.1.1 on 2024-10-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='home_description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات صفحه خانه'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='home_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/about_us', verbose_name='تصویر صفحه خانه'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='home_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='عنوان صفحه خانه'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='tag_1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='تگ 1'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='tag_2',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='تگ 2'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='tag_3',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='تگ 3'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='tag_4',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='تگ 4'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='tag_5',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='تگ 5'),
        ),
    ]
