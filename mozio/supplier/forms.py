from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User

from supplier.models import Supplier


class AddSupplierForm(forms.Form):
    name = forms.CharField(max_length=75, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_no = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '15'}))
    language = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '15'}))
    currency = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '15'}))

    def clean_email(self):
        try:
            existing_user = User.objects.get(email__iexact=self.cleaned_data['email'])
            if existing_user:
                self._errors["email"] = self.error_class(["An Supplier already exists under this email address."])
        except:
            pass

        return self.cleaned_data['email']


class EditSupplierForm(forms.ModelForm):

    class Meta:
        model=Supplier
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
        super(EditSupplierForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['language'].widget.attrs.update({'class': 'form-control'})
        self.fields['currency'].widget.attrs.update({'class': 'form-control'})