# Generated by Django 5.1.1 on 2024-09-25 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0004_alter_sitesettings_phone_alter_sitesettings_whatsapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='is_main_setting',
            field=models.BooleanField(default=False, verbose_name='تنظیمات اصلی'),
        ),
    ]
