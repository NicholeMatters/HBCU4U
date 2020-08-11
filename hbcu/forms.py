from django import forms
from .models import HBCUgrads, College

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User

UserModel = get_user_model()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = UserModel
        fields = ('username', 'first_name','last_name', 'email', 'password1', 'password2', )

class gradForm(forms.ModelForm):
    class Meta:
        model = HBCUgrads
        fields = [
            'first_name',
            'last_name',
            'url',
            'career',
            'date_born',
            'date_died',
            'school',
            'image',
            'history',
        ]
      
class hbcuForm(forms.ModelForm):
    class Meta:
        model = College
        fields = [
            'name',
            'url',
            'major',
            'degree',
            'city',
            'state',
            'technology',
            'financial_aid',
            'logo',
            'campus_image',
            'virtual_tour',
            'history',
      
        ]    

