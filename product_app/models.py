from django.db import models
from django.urls import reverse

class Product(models.Model):
    code = models.CharField(max_length = 20)
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_update', kwargs = {'pk':self.pk})
