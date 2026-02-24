from django import forms

class RegisterForm(forms.Form):
    full_name = forms.CharField(max_length=150)
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    location = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
