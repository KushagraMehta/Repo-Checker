from django import forms
from user.models import UserName

class AddUserForm(forms.ModelForm):
    class Meta():
        model  = UserName
        fields = "__all__"