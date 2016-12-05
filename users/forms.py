from django import forms

class LoginForm(forms.Form):
    user = forms.CharField(widget = forms.TextInput())
    password = forms.CharField(widget = forms.PasswordInput())
