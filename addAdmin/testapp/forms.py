from testapp.models import Admin
from django import forms
class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields =  '__all__'
        # fields = ['name', 'dept',]