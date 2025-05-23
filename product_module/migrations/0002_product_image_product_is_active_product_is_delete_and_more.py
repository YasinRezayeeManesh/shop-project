# Generated by Django 5.1.1 on 2024-09-23 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/products', verbose_name='تصویر'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='فعال / غیرفعال'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='حذف شده / حذف نشده'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100, verbose_name='عنوان'),
        ),
    ]
