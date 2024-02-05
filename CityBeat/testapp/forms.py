from django import forms
import datetime
from datetime import date

class EmployeeForm(forms.Form):
    First_Name = forms.CharField(label='First Name',widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter First Name',
    }))

    Last_Name = forms.CharField(label='Last Name',widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Last Name',
    }))

    roll_No = forms.IntegerField(label='University Roll / Registration Number', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter University Roll / Registration Number',
    }))

    date_of_birth = forms.DateField(
        label='Date of Birth',
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'YYYY-MM-DD',
        })
    )

    
    GENDER_CHOICES = [
        ('', 'Select Gender'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    gender = forms.ChoiceField(
        label='Select Gender',
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs=
                            {'class': 'form-control',
                            }),
    )
    phone_number = forms.CharField(
        label='Phone Number',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Phone Number',
        })
    )

    email_address = forms.EmailField(
        label='Email Address',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Email Address',
        })
    )

    institute_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Institute Name',
        })
    )

    institute_location = forms.CharField(
        label='Institute Location',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Institute Location',
        })
    )

    def clean_First_Name(self):
        First_Name = self.cleaned_data['First_Name']

        if len(First_Name) < 4:
            raise forms.ValidationError('First Name should be at least 4 characters long').color=='red'
        if First_Name and not First_Name[0].isupper():
            raise forms.ValidationError('First Name should start with a capital letter')

        return First_Name
    
    def clean_Last_Name(self):
        Last_Name = self.cleaned_data['Last_Name']
        
        if Last_Name and not Last_Name[0].isupper():
            raise forms.ValidationError('Last Name should start with a capital letter')

        return Last_Name
    
    def clean_roll_No(self):
        roll_No = self.cleaned_data['roll_No']

        if roll_No <0 :
            raise forms.ValidationError('University Roll / Registration Number cannot be negative or Zeor')
        return roll_No
    
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']

        if date_of_birth < datetime.date(1990, 1, 1):
            raise forms.ValidationError('Date of Birth cannot be before 1990-01-01')
        return date_of_birth
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        if len(phone_number) != 10:
            raise forms.ValidationError('Phone Number should be 10 digits long')
        
    def clean_email_address(self):
        email_address = self.cleaned_data['email_address']

        if len(email_address) >= 10 and email_address.lower().endswith('@gmail.com'):
            return email_address
        else:
            raise forms.ValidationError('Email Address should end with @gmail.com')


