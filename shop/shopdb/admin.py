from django.contrib import admin
from .models import ItemGroupCatalog
from .models import ProductAttribute
from .models import Client

# Register your models here.

admin.site.register(ItemGroupCatalog)
admin.site.register(ProductAttribute)
admin.site.register(Client)
