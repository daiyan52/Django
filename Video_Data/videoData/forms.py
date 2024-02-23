from django import forms
from .models import videoData

class videoDataForm(forms.ModelForm):
    class Meta:
        model = videoData
        fields = '__all__'