from django import forms
from django.forms import fields

from leads.models import Lead

class LeadForm(forms.ModelForm):
    
    class Meta:
        model = Lead
        fields = ["first_name", "last_name", "age"]