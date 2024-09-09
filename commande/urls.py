from django.urls import path 
from . import views 


urlpatterns = [
    path('commande/', views.checkout, name='commande'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('delivery/', views.delivery, name='delivery'),
]