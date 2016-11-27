# shop

2016.11.23

---

sukurem project: django-admin startproject shop
migruojam lenteles:
python manage.py makemigrations shopdb
python manage.py sqlmigrate shopdb 0001
python manage.py migrate
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

sukurta productattributes klase su modeliais

**foreign key nauodojimas:**
    itemgroupcatalog = models.ForeignKey(ItemGroupCatalog, on_delete=models.CASCADE)
    def __str__(self):
        return self.itemgroupcatalog
        
sukurta kliento lentele, migruota

**drop-down listas lyciai kliento lyciai pasirinkti:**
GENDER = (
    ('FEMALE', 'female'),
    ('MALE', 'male'),
)

kai atvaizduoti kelis kintamuosius:
    def __str__(self):
        return "%s %s" % (self.fname, self.lname)
        
kai atvaizduojame ID, pvz prie card number:
    def __int__(self):
        return self.id