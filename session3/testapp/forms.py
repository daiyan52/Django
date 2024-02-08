from django import forms

class addItemForm(forms.Form):
    itemName = forms.CharField(label='Item Name',widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Item Name',
        'style': 'width: 50%;'  
    }))

    quantity = forms.IntegerField(label='Quantity',widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Quantity',
        'style': 'width: 50%;' 

    }))