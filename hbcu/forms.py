from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget



CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = CustomUser
        fields = ('username', 'birth_date', 'password1', 'password2', )

class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ("coordinates", "city_hall")
        widgets = {
            'coordinates': GooglePointFieldWidget,
            'city_hall': GoogleStaticOverlayMapWidget,
