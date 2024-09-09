from django.db import models
from django.contrib.auth.models import AbstractUser

class Client(AbstractUser):
    adresse_livraison = models.CharField(max_length=100,default="")
    adresse = models.CharField(max_length=100,default="")
    telephone = models.CharField(max_length=20,default="")
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ['username']

    def __str__(self):
        return self.username
    


