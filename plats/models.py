from django.db import models
from django.contrib import admin
from clients.models import Client
# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.nom

    def get_plats(self):
        return Plat.objects.filter(Categorie=self)

class Plat(models.Model):
   
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE,default="")
    actif=models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.pk} {self.nom} {self.prix} {self.categorie} {self.actif}"
    
    @property
    def comments(self):
        return Comment.objects.filter(plat=self)



class PlatAdmin(admin.ModelAdmin):
    list_display= ('nom','prix','categorie','actif')
    

class Comment(models.Model):
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Comment by {self.client.username} on {self.plat.nom}"









    

