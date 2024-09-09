from django.db import models
from plats.models import Plat
from django.contrib import admin
# Create your models here.
class Panier(models.Model):
    proprietaire = models.OneToOneField('clients.Client', on_delete=models.CASCADE)
    plat = models.ManyToManyField(Plat, through='ListePlat', related_name='paniers')


    def __str__(self):
        return f"panier {self.pk} - Propriétaire: {self.proprietaire.username}"
    
    def liste_plats(self):
        return self.plat.all()

    def calculer_total(self):
        total = 0
        lignes_panier = ListePlat.objects.filter(panier=self)
        for ligne_panier in lignes_panier:
            total += ligne_panier.quantite_commandee * ligne_panier.plat.prix
        return total
    
class ListePlat(models.Model):
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)
    quantite_commandee = models.PositiveIntegerField(default=1)
    def get_produits_panier(self):
        return self.plat.all()

class PanierAdmin(admin.ModelAdmin):
    list_display=('pk','proprietaire_nom')

    def proprietaire_nom(self, obj):
        return obj.proprietaire.username
    proprietaire_nom.short_description = "Nom du propriétaire"


class ListePlatAdmin(admin.ModelAdmin):
    list_display = ('get_plat_nom', 'quantite_commandee', 'panier_proprietaire_nom')

    def get_plat_nom(self, obj):
        return obj.plat.nom

    get_plat_nom.short_description = "Nom du plat"

    def panier_proprietaire_nom(self, obj):
        return obj.panier.proprietaire.username

    panier_proprietaire_nom.short_description = "Nom du propriétaire du panier"


class Wishlist(models.Model):
    proprietaire = models.OneToOneField('clients.Client', on_delete=models.CASCADE)
    produits = models.ManyToManyField(Plat)

    def __str__(self):
        return f"Wishlist {self.pk} - Propriétaire: {self.proprietaire.username}"

    def get_produits(self):
        return self.produits.all()
    
    def ajouter_plat(self, plat):
        self.produits.add(plat)

    def supprimer_plat(self, plat):
        self.produits.remove(plat)


class WishlistAdmin(admin.ModelAdmin):
    list_display = ("pk", "proprietaire_nom")

    def proprietaire_nom(self, obj):
        return obj.proprietaire.username
    proprietaire_nom.short_description = "Nom du propriétaire"