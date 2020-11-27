# to add new fields to the form that are not default
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.TextInput(None)
    last_name = forms.TextInput(None)

    # this Meta class is so you can specify the models this form must interect with
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.TextInput(None)
    last_name = forms.TextInput(None)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    image = ProcessedImageField(spec_id='accounts:profile:image',
                                processors=[ResizeToFill(300, 300)],
                                format='JPEG',
                                options={'quality': 60})

    class Meta:
        model = Profile
        fields = ['image']


    