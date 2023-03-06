from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ShoppingCartDatabase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    slug = models.SlugField()
    def __str__(self):
        return self.product