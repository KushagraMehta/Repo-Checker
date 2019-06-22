from django import forms
from django.core import validators
import requests


def find_user(username):
    r = requests.get('https://api.github.com/users/'+username+'/repos')
    return False if r.status_code == 404 else True


class user_name(forms.Form):
    user = forms.CharField(required=True,
                           label="",
                           widget=forms.TextInput(attrs={'class': 'input100'})
                           )

    def clean_user(self):
        username = self.cleaned_data.get('user')

        if not find_user(username):
            raise forms.ValidationError("Enter correct UserName")

        return username
