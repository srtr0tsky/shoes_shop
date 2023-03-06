from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=30)
    quantify = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_product = models.ImageField(upload_to='images/')
    image_product1 = models.ImageField(upload_to='images/')
    image_product2 = models.ImageField(upload_to='images/')
    image_product3 = models.ImageField(upload_to='images/')
    amount_sales = models.PositiveIntegerField(default=0)
    seller = models.CharField(max_length=30)
    slug = models.SlugField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.product_name
    def save(self):
        self.slug = slugify(self.product_name)
        return super(Product, self).save()

