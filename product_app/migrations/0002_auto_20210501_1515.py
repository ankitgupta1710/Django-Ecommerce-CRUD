# Generated by Django 3.2 on 2021-05-01 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='email',
        ),
        migrations.RemoveField(
            model_name='product',
            name='phone',
        ),
        migrations.AddField(
            model_name='product',
            name='availablity',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='categoty',
            field=models.CharField(blank=True, choices=[('1', 'Electronics'), ('2', 'Household'), ('3', 'Clothing'), ('4', 'FOOD')], max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='product',
            name='offers',
            field=models.CharField(default='NO OFFER', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(db_column='Image', default='1.png', upload_to='img/'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=6),
        ),
    ]