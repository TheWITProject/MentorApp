from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *

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
        fields = ('first_name', 'last_name','profile_pic', 'phone', 'user_type','title','company','county','county','gender','ethnicity','education','industry','learningtrack','linkedin','funfact' ) 
    def __init__(self, *args, **kwargs):
            super(ProfileForm, self).__init__(*args, **kwargs)
            for field in iter(self.fields):
                if field is not 'profile_pic':
                    self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })

# class FrequentlyAskedForm(forms.ModelForm):
#     class Meta:
#         model = FrequentlyAsked
#         fields = ('question', 'answer',)