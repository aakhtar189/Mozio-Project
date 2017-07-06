from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=75, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get("email", "")
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address does not exists!")
        return cleaned_data