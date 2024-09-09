from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('subscribe-newsletter', views.subscribe_newsletter, name='subscribe_newsletter'),

]