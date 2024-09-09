from django.contrib import admin
from .models import Panier,PanierAdmin
from .models import ListePlat,ListePlatAdmin
from .models import Wishlist, WishlistAdmin

# Register your models here.

admin.site.register(Panier,PanierAdmin)
admin.site.register(ListePlat,ListePlatAdmin)
admin.site.register(Wishlist, WishlistAdmin)
