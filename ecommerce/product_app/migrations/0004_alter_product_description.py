# Generated by Django 3.2 on 2021-05-01 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0003_rename_categoty_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=' '),
        ),
    ]
