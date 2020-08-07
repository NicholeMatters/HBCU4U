from django import forms
from .models import HBCUgrads, College

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget

CustomUser = get_user_model()

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = CustomUser
        fields = ('username', 'birth_date', 'password1', 'password2', )

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

class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ("coordinates", "city_hall")
        widgets = {
            'coordinates': GooglePointFieldWidget,
            'city_hall': GoogleStaticOverlayMapWidget,
        }