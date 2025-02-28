from django import forms
from . models import Customer, Contact
from bootstrap_datepicker_plus.widgets import DatePickerInput

class DataForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
        widgets={
            'InsuranceDuration':DatePickerInput()
        } 

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']