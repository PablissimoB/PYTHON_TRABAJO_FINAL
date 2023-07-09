from django import forms
from .models import Profile
from django.contrib.auth.models import User

class ProfileEditForm(forms.Form):
    imagen = forms.ImageField(required=False)
    city = forms.CharField()
    country = forms.CharField()

class UserEditForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields=['last_name','first_name','email','password']