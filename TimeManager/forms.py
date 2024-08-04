from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import WorkEntry


class WorkEntryForm(forms.ModelForm):
    class Meta:
        model = WorkEntry
        fields = ['job_title', 'hours_worked', 'comment', 'hourly_rate', 'date']  # Добавьте это поле
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'hours_worked': forms.NumberInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'hourly_rate': forms.NumberInput(attrs={'class': 'form-control'}),  # Добавьте это поле
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
