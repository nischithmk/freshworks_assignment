from django import forms
from .models import table1

class SomeForm(forms.ModelForm):
    class Meta:
        model = table1
        fields = '__all__'
