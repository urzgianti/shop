from django.db import models

class Basket(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Product(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(Basket)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)