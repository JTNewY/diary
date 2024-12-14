from django import forms
from .models import Holiday

class HolidayForm(forms.ModelForm):
    class Meta:
        model = Holiday
        fields = ['H_name', 'H_date', 'H_memo', 'H_country']