from django import forms

class nameForm(forms.Form):
    name = forms.CharField()

class rollNumberForm(forms.Form):
    rollNumber = forms.IntegerField()


class deptForm(forms.Form):
    dept = forms.CharField()