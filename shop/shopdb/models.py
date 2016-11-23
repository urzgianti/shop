from django.db import models

GENDER = (
    ('FEMALE', 'female'),
    ('MALE', 'male'),
)

# Create your models here.

class ItemGroupCatalog(models.Model):
    item_group = models.CharField(max_length=200)
    def __str__(self):
        return self.item_group

class ProductAttribute(models.Model):
    itemgroupcatalog = models.ForeignKey(ItemGroupCatalog, on_delete=models.CASCADE)
    def __str__(self):
        return self.itemgroupcatalog

    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

    size = models.CharField(max_length=200)
    def __str__(self):
        return self.size

    price = models.CharField(max_length=200)
    def __str__(self):
        return self.price

    brand = models.CharField(max_length=200)
    def __str__(self):
        return self.brand

class Client(models.Model):
    fname = models.CharField(max_length=200)
    def __str__(self):
        return self.fname

    lname = models.CharField(max_length=200)
    def __str__(self):
        return self.lname

    gender = models.CharField(max_length=6, choices=GENDER)
    def __str__(self):
        return self.gender

    bdate = models.DateField()
    def __str__(self):
        return self.bdate

    telephone = models.CharField(max_length=200)
    def __str__(self):
        return self.telephone

    email = models.CharField(max_length=200)
    def __str__(self):
        return self.email

    city = models.CharField(max_length=200)
    def __str__(self):
        return self.city

class Card(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    def __str__(self):
        return self.client

    discount = models.CharField(max_length=200)
    def __str__(self):
        return self.discount

    issued = models.DateField()
    def __str__(self):
        return self.issued

    expires = models.DateField()
    def __str__(self):
        return self.expires

class Shop(models.Model):
    shopname = models.CharField(max_length=200)
    def __str__(self):
        return self.shopname

    address = models.CharField(max_length=200)
    def __str__(self):
        return self.address

    shopphone = models.CharField(max_length=200)
    def __str__(self):
        return self.shopphone

class Employee(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    def __str__(self):
        return self.shop

    efname = models.CharField(max_length=200)
    def __str__(self):
        return self.efname

    elname = models.CharField(max_length=200)
    def __str__(self):
        return self.elname

    egender = models.CharField(max_length=6, choices=GENDER)
    def __str__(self):
        return self.egender

    ebdate = models.DateField()
    def __str__(self):
        return self.ebdate

    ephone = models.CharField(max_length=200)
    def __str__(self):
        return self.ephone

    eemail = models.CharField(max_length=200)
    def __str__(self):
        return self.eemail

class Order(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    def __str__(self):
        return self.shop

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    def __str__(self):
        return self.client

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    def __str__(self):
        return self.employee

    collection_date = models.DateField()
    def __str__(self):
        return self.collection_date

