from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
          "firstname", 
          "lastname",
          "email", 
          "city",
          "state",
          ]

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
