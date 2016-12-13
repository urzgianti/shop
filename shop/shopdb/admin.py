from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(ItemGroupCatalog)
class ItemGroupCatalogAdmin(admin.ModelAdmin):
    list_display = ("item_group",)
    search_fields = ("item_group",)
    list_filter = ("item_group",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("itemgroupcatalog", "name", "size", "price", "brand")
    search_fields = ("itemgroupcatalog__item_group", "name", "size", "price", "brand")
    list_filter = ("itemgroupcatalog__item_group", "name", "size", "price", "brand")

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("fname", "lname", "gender", "bdate", "telephone", "email", "city")
    search_fields = ("fname", "lname", "gender", "bdate", "telephone", "email", "city")
    list_filter = ("fname", "lname", "gender", "bdate", "city")

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('client', 'discount', 'issued', 'expires')
    search_fields = ('client__fname', "client__lname", 'discount', 'issued', 'expires')
    list_filter = ('client__fname', "client__lname", 'discount', 'issued', 'expires')

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ["shopname", "address", "shopphone",]
    search_fields = ["shopname", "address", "shopphone",]
    list_filter = ["shopname", "address", "shopphone",]

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["shop", "efname", "elname", "egender", "ebdate", "ephone", "eemail"]
    search_fields = ["shop__shopname", "efname", "elname", "egender", "ebdate", "ephone", "eemail"]
    list_filter = ["shop__shopname", "efname", "elname", "egender"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "shop", "client", "employee", "collection_date")
    search_fields = ("id", "shop__shopname", 'client__fname', "client__lname", "employee__efname", "employee__elname", "collection_date")
    list_filter = ("id", "shop__shopname", 'client__fname', "client__lname", "employee__efname", "employee__elname", "collection_date")

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ("id", "clientother")
    search_fields = ("id", "client__fname")
    list_filter = ("id", "client__fname")



