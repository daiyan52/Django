from django import forms
from captcha.fields import CaptchaField

class studentForm(forms.Form):
    name = forms.CharField()
    captcha = CaptchaField()