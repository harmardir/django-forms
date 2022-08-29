from django import forms
from django.forms import ModelForm
from .models import User
from django.contrib.auth.hashers import make_password

class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    def save(self):
        pass

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password', 'email']
    def save(self, commit=True, *args, **kwargs):
        m = super().save(commit=False)
        m.password = make_password(self.cleaned_data.get('password'))
        m.username = self.cleaned_data.get('username').lower()

        if commit:
            m.save()
        return m
    
