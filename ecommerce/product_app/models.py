from django.db import models
from django.urls import reverse
OFFERS = [('Offer 1','Offer 1'),('Offer 2','Offer 2'), ('Offer 3','Offer 3'),('Offer 4','Offer 4')]
DELIVERY_OPTIONS = [('1-Day','1-Day'),('2-Day','2-Day'), ('5-Day','5-Day'),('10-Days (Free)','10-Days (Free)')]
class Product(models.Model):
    code = models.CharField(max_length = 20)
    name = models.CharField(max_length=100)
    description = models.TextField(default = ' ')
    price = models.DecimalField(max_digits=6,decimal_places=2, default = '0')
    photo = models.ImageField(upload_to='img/',default = '1.png', db_column='Image')
    manufacturer = models.CharField(max_length=300,blank=True)
    offers = models.CharField(max_length=200,default='NO OFFER')
    delivery_options = models.CharField(max_length=200,default='4-days')
    availablity = models.BooleanField(default=False)
    CATEGORY =[('Electronics','Electronics'),('Household','Household'),('Clothing','Clothing'),('FOOD','FOOD')]
    category = models.CharField(choices=CATEGORY,max_length=100,blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_update', kwargs = {'pk':self.pk})
