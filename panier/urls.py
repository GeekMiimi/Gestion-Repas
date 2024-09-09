from django.urls import path 
from . import views


urlpatterns = [
    path('panier/', views.panier, name= 'panier'),
    path('panier/ajouter/<int:plat_id>/', views.ajouter_panier, name='ajouter_panier'),
    path('panier/supprimer/<int:plat_id>/', views.supprimer_panier, name='supprimer_panier'),
    path('panier/incrementer/<int:ligne_panier_id>/', views.incrementer_quantite, name='incrementer_quantite'),
    path('panier/decrementer/<int:ligne_panier_id>/', views.decrementer_quantite, name='decrementer_quantite'),
    path('wishlist/ajouter/<int:plat_id>/', views.ajouter_wishlist_view, name='ajouter_wishlist'),
    path('wishlist/supprimer/<int:plat_id>/', views.supprimer_wishlist_view, name='supprimer_wishlist'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
]