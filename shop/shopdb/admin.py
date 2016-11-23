from django.contrib import admin
from .models import ItemGroupCatalog
from .models import ProductAttribute
from .models import Client
from .models import Card
from .models import Shop
# Register your models here.

admin.site.register(ItemGroupCatalog)
admin.site.register(ProductAttribute)
admin.site.register(Client)
admin.site.register(Card)
admin.site.register(Shop)