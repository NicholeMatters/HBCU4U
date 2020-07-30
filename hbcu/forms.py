from django import forms
from .models import Contact,


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
