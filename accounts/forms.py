# forms.py in accounts app

from django import forms
from .models import Profile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email_token',]  # Add other fields as needed
