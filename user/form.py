from django import forms
from django.core import validators
from django.forms import ValidationError
import requests


class user_name(forms.Form):
    user = forms.CharField(required=True,
                           label="",
                           widget=forms.TextInput(attrs={'class': 'input100'})
                           )

    def clean_user(self):
        username = self.cleaned_data.get('user')
        r = requests.get('https://api.github.com/users/' + username + '/repos')

        if r.status_code == 404:
            raise ValidationError(
                "Enter correct UserName",
                code='invalid')
        return username
