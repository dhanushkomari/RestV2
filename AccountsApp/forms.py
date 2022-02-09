from .models import CustomUser as User
from django import forms

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'Chef', 'Category')
        widgets = {
            'Chef' : forms.CheckboxSelectMultiple,
            'Category' : forms.CheckboxSelectMultiple,

        }