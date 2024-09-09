from django.urls import path 
from . import views 


urlpatterns = [
    path('plat/<int:id>', views.plat, name= 'plat'),
    path('', views.plats, name= 'plats'),
    path('search/', views.search, name='search'),
    path('plat/<int:id>/', views.plat_details, name='plat_details'),
]