# shop

2016.11.23

---

sukurem project: django-admin startproject shop
paleidom appsą su: python manage.py runserver
sukūrėm .gitignore, kuriame extensions, kokius failus pucharmui ignoruot (.idea - pycharm nustatymai; .pyc - c failai pritaikyti pythonui)
pirma lentelė ItemGroup
superuser: admin
pass: adminadmin

sukurtas atvaizdavimas admine ir lenteliu kurimas:
class ItemGroupCatalog(models.Model):
    item_group = models.CharField(max_length=200)
    def __str__(self):
        return self.item_group
 
idejom dvi prekiu grupes: veidas ir kunas
