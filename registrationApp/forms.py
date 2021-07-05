from django.contrib.auth.forms import AuthenticationForm
from django import forms

class SignUpForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control bg-white border-left-0 border-md'}))