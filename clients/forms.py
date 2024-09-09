from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Client
from django.contrib.auth.forms import UserChangeForm


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

    class Meta:
        model = Client
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'adresse_livraison', 'adresse', 'telephone')

class LoginForm(AuthenticationForm):
    pass



class ClientProfileForm(UserChangeForm):
    password = None  

    class Meta:
        model = Client
        fields = ('username', 'first_name', 'last_name', 'email', 'adresse_livraison', 'adresse', 'telephone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'] = forms.CharField(label='Password', widget=forms.PasswordInput)
        self.fields['password'].help_text = self.fields['password'].help_text.replace(
            'optional', 'optional. Enter a valid password or leave it blank to keep the current password.'
        )

