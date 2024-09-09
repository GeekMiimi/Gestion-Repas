from django.contrib import admin
from .models import Plat, PlatAdmin,Comment,Categorie
# Register your models here.

admin.site.register(Plat,PlatAdmin)
admin.site.register(Comment)
admin.site.register(Categorie)

