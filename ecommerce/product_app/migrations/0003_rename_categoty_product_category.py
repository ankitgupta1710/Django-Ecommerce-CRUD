# Generated by Django 3.2 on 2021-05-01 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0002_auto_20210501_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categoty',
            new_name='category',
        ),
    ]
