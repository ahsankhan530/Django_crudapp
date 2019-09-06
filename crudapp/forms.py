from crudapp.models import registrations
from django import forms
class registrationForm(forms.ModelForm):
    class Meta:
        model=registrations
        fields="__all__"