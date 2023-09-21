from django import forms
from .models import Gsk

class TaskForm(forms.ModelForm):
    class Meta:
        model=Gsk
        fields=['Patient_name','Patient_ID','Patient_address','Patient_Bill']
