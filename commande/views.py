from django.shortcuts import render, redirect
from .forms import CheckoutForm
from .models import Commande, Promotion
from django.contrib.auth.decorators import login_required


@login_required
def checkout(request):
    client = request.user
    panier = client.panier
    total_price = panier.calculer_total() + 15

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            delivery_address = form.cleaned_data['delivery_address']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            payment_method = form.cleaned_data['payment_method']
            promotion_code = form.cleaned_data['promotion_code']

            try:
                promotion = Promotion.objects.get(code=promotion_code)
            except Promotion.DoesNotExist:
                promotion = None

            if promotion:
                total_price -= (promotion.reduction * total_price) / 100

            commande_obj = Commande.objects.create(
                panier=panier,
                client=client,
                name=name,
                delivery_address=delivery_address,
                email=email,
                phone=phone,
                total_amount=total_price,
                payment_method=payment_method,
                promotion=promotion
            )

            for item in panier.listeplat_set.all():
                quantity = item.quantite_commandee
                commande_obj.add_ordered_item(item.plat, quantity)

            commande_obj.process_payment()

            if payment_method == 'cash_on_delivery':
                return redirect('confirmation')
            elif payment_method == 'credit_card':
                return redirect('confirmation')
    else:
        form = CheckoutForm()

    products = panier.listeplat_set.all()

    context = {
        'total_price': total_price,
        'form': form,
        'liste_plats': products
    }
    return render(request, 'commande/commande.html', context)


@login_required
def confirmation(request):
    commande_obj = Commande.objects.latest('pk')
    ordered_items = commande_obj.commandeitem_set.all()

    commande_obj.confirm_order()
    context = {
        'commande_obj': commande_obj,
        'ordered_items': ordered_items
    }

    return render(request, 'commande/confirmation.html', context)


@login_required
def delivery(request):
    commande_obj = Commande.objects.latest('pk')
    panier = commande_obj.panier
    panier.delete()

    context = {
        'commande_obj': commande_obj
    }

    return render(request, 'commande/delivery.html', context)

