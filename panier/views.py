from django.shortcuts import render,redirect
from .models import Wishlist,Panier,ListePlat
from clients.models import Client
from plats.models import Plat
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def wishlist_view(request):
    try:
        client = Client.objects.get(username=request.user.username)
        wishlist = client.wishlist
        produits = wishlist.get_produits()
        return render(request, 'panier/wishlist.html', {'produits': produits})
    except Wishlist.DoesNotExist:
        return render(request, 'panier/wishlist.html')


@login_required
def ajouter_wishlist_view(request, plat_id):
    client = Client.objects.get(username=request.user.username)
    try:
        wishlist = client.wishlist
    except Wishlist.DoesNotExist:
        wishlist = Wishlist.objects.create(proprietaire=client)
    plat = Plat.objects.get(id=plat_id)
    wishlist.ajouter_plat(plat)
    return redirect(request.META['HTTP_REFERER'])

@login_required
def supprimer_wishlist_view(request, plat_id):
    client = Client.objects.get(username=request.user.username)
    plat = Plat.objects.get(id=plat_id)
    wishlist = client.wishlist
    wishlist.supprimer_plat(plat)
    return redirect(request.META['HTTP_REFERER'])


def panier(request):
    if request.user.is_authenticated:
        try:
            client = Client.objects.get(username=request.user.username)
            panier = Panier.objects.get(proprietaire=client)
            lignes_panier = ListePlat.objects.filter(panier=panier)
            wishlist_produits = request.user.wishlist.produits.all() if request.user.is_authenticated else []
            nombre_total_plats = lignes_panier.aggregate(total=Sum('quantite_commandee'))['total']
            for ligne_panier in lignes_panier:
                ligne_panier.total_plat = ligne_panier.quantite_commandee * ligne_panier.plat.prix
            total_panier = sum(ligne_panier.total_plat for ligne_panier in lignes_panier)
            return render(request, 'panier/panier.html', {'lignes_panier': lignes_panier, 'nombre_total_plats': nombre_total_plats, 'total_panier': total_panier, 'wishlist_produits': wishlist_produits})
        except Panier.DoesNotExist:
            return render(request, 'panier/panier.html')
    else:
        return redirect('login')



@login_required
def ajouter_panier(request, plat_id):
    client = Client.objects.get(username=request.user.username)
    try:
        panier = Panier.objects.get(proprietaire=client)
    except Panier.DoesNotExist:
        panier = Panier.objects.create(proprietaire=client)

    plat = Plat.objects.get(id=plat_id)
    ligne_panier, created = ListePlat.objects.get_or_create(panier=panier, plat=plat)

    if not created:
        ligne_panier.quantite_commandee += 1
        ligne_panier.save()

    return redirect(request.META['HTTP_REFERER'])

@login_required
def supprimer_panier(request, plat_id):
    try:
        lignes_panier = ListePlat.objects.filter(plat_id=plat_id)
        lignes_panier.delete()
    except ListePlat.DoesNotExist:
        pass 

    return redirect(request.META['HTTP_REFERER'])



def incrementer_quantite(request, ligne_panier_id):
    try:
        ligne_panier = ListePlat.objects.get(id=ligne_panier_id)
        ligne_panier.quantite_commandee += 1
        ligne_panier.save()
    except ListePlat.DoesNotExist:
        pass 

    return redirect(request.META['HTTP_REFERER'])


def decrementer_quantite(request, ligne_panier_id):
    try:
        ligne_panier = ListePlat.objects.get(id=ligne_panier_id)
        if ligne_panier.quantite_commandee > 1:
            ligne_panier.quantite_commandee -= 1
            ligne_panier.save()
        elif ligne_panier.quantite_commandee == 1:
            ligne_panier.delete()
    except ListePlat.DoesNotExist:
        pass  
    return redirect(request.META['HTTP_REFERER'])


@receiver(post_save, sender=Client)
def create_wishlist(sender, instance, created, **kwargs):
    if created:
        Wishlist.objects.create(proprietaire=instance)