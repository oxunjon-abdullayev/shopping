# Generated by Django 4.2.1 on 2023-07-31 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_name_post_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image4',
        ),
    ]
