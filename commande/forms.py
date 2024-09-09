from django import forms

PAYMENT_CHOICES = [
    ('cash_on_delivery', 'Cash on Delivery'),
    ('credit_card', 'Credit Card'),
]

class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=100)
    delivery_address = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    payment_method = forms.ChoiceField(choices=PAYMENT_CHOICES, widget=forms.RadioSelect)
    promotion_code = forms.CharField(max_length=20, required=False)
