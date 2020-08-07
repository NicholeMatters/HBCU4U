from django import forms
from .models import HBCUgrads, College

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


from hbcu.models import City
from mapwidgets.widgets import GooglePointFieldWidget,GoogleStaticOverlayMapWidget, GoogleStaticMapWidget



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

class CityCreateForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ("name", "coordinates", "city_hall")
        fields = ('name', 'location')
        widgets = {
            'coordinates': GooglePointFieldWidget,
            'city_hall': GooglePointFieldWidget,
            'location': GooglePointFieldWidget,
        }


class CityDetailForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ("name", "coordinates", "city_hall")
        fields = ('name', 'location')
        widgets = {
            'coordinates': GoogleStaticMapWidget(zoom=12, size="240x240"),
            'city_hall': GoogleStaticOverlayMapWidget(zoom=12, thumbnail_size="50x50", size="640x640"),
            'location': GoogleStaticOverlayMapWidget(zoom=12, thumbnail_size='50x50', size='640x640'),
        }
