from PIL import Image
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile
from django.core.files import File

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Please provide a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        managed = True

class ProfileForm(forms.ModelForm):
    #defining variables for cropping the image
    x = forms.FloatField(widget=forms.HiddenInput())   #x coordinate of where the cropfield is
    y = forms.FloatField(widget=forms.HiddenInput())   #y coordinate of where cropfield is
    width = forms.FloatField(widget=forms.HiddenInput())    #width of cropbox
    height = forms.FloatField(widget=forms.HiddenInput())   #heigh of cropbox

    class Meta:
        model = Profile
        phone = model.phone
        fields = ('first_name', 'last_name','profile_pic', 'phone', 'user_type','job_title','company','county','county','gender_pronouns','ethnicity','education','industry','learningtrack','linkedin','funfact', 'cohort', 'site_location', 'x', 'y', 'width', 'height' )
    def __init__(self, *args, **kwargs):
            super(ProfileForm, self).__init__(*args, **kwargs)
            for field in iter(self.fields):
                if field is not 'profile_pic':
                    self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })

    #saving values of x,y,w,h of the photo that user uploads
    #implementation is for the cropper box
    def save(self):
        photo = super(ProfileForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.profile_pic)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        resized_image.save(photo.profile_pic.path)

        return photo
