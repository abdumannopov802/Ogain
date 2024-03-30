from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer

class UserAdminCreationForm(UserCreationForm):
    address = forms.CharField(max_length=255, required=False)
    phone_number = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'address', 'phone_number']
