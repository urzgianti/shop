from django.contrib import admin

from .models import ItemGroupCatalog
from .models import Product
from .models import Client
from .models import Card
from .models import Shop
from .models import Employee
from .models import Order
from .models import Basket

# Register your models here.


admin.site.register(ItemGroupCatalog)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Card)
admin.site.register(Shop)
admin.site.register(Employee)
admin.site.register(Order)
admin.site.register(Basket)
