from django import forms

class loginForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control w-25',
        'placeholder': 'Enter Name',
    }))
