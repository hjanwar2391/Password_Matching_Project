from django import forms
from django.core.exceptions import ValidationError
from django.core import validators



class Student(forms.Form):
    studenName = forms.CharField(validators=[validators.MinLengthValidator(10, message='enter the mane must 10 char')])


class PasswordChack(forms.Form):
    userName = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['userName']

        if val_pass != val_conpass:
            raise forms.ValidationError('password does not match')
        if len(val_name) < 15:
            raise forms.ValidationError('name must be at least 15 characters')