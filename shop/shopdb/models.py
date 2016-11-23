from django.db import models

# Create your models here.

class ItemGroupCatalog(models.Model):
    item_group = models.CharField(max_length=200)
    def __str__(self):
        return self.item_group

class ProductAttributes(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

    size = models.CharField(max_length=200)
    def __str__(self):
        return self.size

    price = models.FloatField
    def __str__(self):
        return self.price

    brand = models.CharField(max_length=200)
    def __str__(self):
        return self.brand
