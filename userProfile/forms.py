from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Please provide a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        managed = True

class ProfileForm(forms.ModelForm):
     class Meta:
         model = Profile
         phone = model.phone
         fields = ('first_name', 'last_name', 'phone', ) #Note that we didn't mention user field here.