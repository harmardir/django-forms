from django import forms
from django.forms import ModelForm
from .models import User

class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    def save(self):
        pass

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']