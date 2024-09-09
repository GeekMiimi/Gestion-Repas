from django.db import models
from clients.models import Client 
from django.utils import timezone

class Commande(models.Model):
    STATUS_CHOICES = [
        ('Waiting_for_confirmation', 'Waiting for confirmation'),
        ('Confirmed', 'Confirmed'),
        ('In_the_course_of_delivery', 'In the course of delivery'),
        ('Delivered', 'Delivered'),
    ]
    panier = models.ForeignKey('panier.Panier', on_delete=models.SET_NULL, null=True,blank=True)
    name = models.CharField(max_length=100, default="")
    delivery_address = models.CharField(max_length=200, default="")
    email = models.EmailField(default="")
    total_amount = models.FloatField(default=0)
    phone = models.CharField(max_length=20, default="")
    payment_method = models.CharField(max_length=50, default="")
    ordered_items = models.ManyToManyField('plats.Plat', through='CommandeItem')
    client = models.ForeignKey(Client, on_delete=models.CASCADE,null=True)  
    statut= models.CharField(max_length=50, choices=STATUS_CHOICES, default='Waiting_for_confirmation')
    date = models.DateTimeField(default=timezone.now)
    promotion = models.ForeignKey('commande.Promotion', on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        panier_id = self.panier.pk if self.panier else None
        return f"Commande {self.pk} - Panier: {panier_id}"

    def process_payment(self):
        if self.payment_method == 'cash_on_delivery':
            self.payment_status = True
            self.save()
        elif self.payment_method == 'credit_card':
            self.payment_status = True
            self.save()
        else:
            raise ValueError("Unsupported payment method")

    def add_ordered_item(self, item, quantity):
        CommandeItem.objects.create(commande=self, item=item, quantity=quantity)
    
    def confirm_order(self):
        self.statut = 'Confirmed'
        self.save()



class CommandeItem(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    item = models.ForeignKey('plats.Plat', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Promotion(models.Model):
    code = models.CharField(max_length=50, unique=True)
    reduction = models.DecimalField(max_digits=5,decimal_places=2)
    
    def __str__(self):
        return self.code