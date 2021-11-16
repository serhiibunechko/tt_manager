from .models import Process
from django.forms import ModelForm, TextInput, Textarea


class ProcessForm(ModelForm):
    class Meta:
        model = Process
        fields = ["topic", "basis"]
        widgets = {
            "topic": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add topic'
            }),
            "basis": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe process'
            }),
        }
