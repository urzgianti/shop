from django.contrib import admin
from .models import ItemGroupCatalog
from .models import ProductAttribute
from .models import Client
from .models import Card
from .models import Shop
from .models import Employee
from .models import Order
# Register your models here.

admin.site.register(ItemGroupCatalog)
admin.site.register(ProductAttribute)
admin.site.register(Client)
admin.site.register(Card)
admin.site.register(Shop)
admin.site.register(Employee)
admin.site.register(Order)