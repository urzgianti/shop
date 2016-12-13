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

class Product(models.Model):

    itemgroupcatalog = models.ForeignKey(ItemGroupCatalog, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Client(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=6, choices=GENDER)
    bdate = models.DateField()
    telephone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s" % (self.fname, self.lname)



class Card(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    discount = models.CharField(max_length=200)
    issued = models.DateField()
    expires = models.DateField()

    def __str__(self):
        return self.client

class Shop(models.Model):
    shopname = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    shopphone = models.CharField(max_length=200)

    def __str__(self):
        return self.shopname

class Employee(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    efname = models.CharField(max_length=200)
    elname = models.CharField(max_length=200)
    egender = models.CharField(max_length=6, choices=GENDER)
    ebdate = models.DateField()
    ephone = models.CharField(max_length=200)
    eemail = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s" % (self.efname, self.elname)

class Order(models.Model):

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    collection_date = models.DateField()
    id = models.AutoField(primary_key=True)

    def __int__(self):
        return self.id

    def __str__(self):
        return "order {}".format(self.id)

class Basket(models.Model):
    product = models.ManyToManyField(Product)
    client = models.ManyToManyField(Client)
    id = models.AutoField(primary_key=True)
    # FIXME: needs some filtering



    #def __int__(self):
    #   return self.id

    def __str__(self):
        return "basket {}".format(self.id)


