from django import forms

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
        label='',
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

