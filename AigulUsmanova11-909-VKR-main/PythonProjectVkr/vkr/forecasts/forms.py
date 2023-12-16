from .models import Models
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ModelsForm(ModelForm):
    class Meta:
        model = Models
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название прогноза'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Прогнозируемая сущность'
            }),
            "date": DateTimeInput(attrs={
                'type': "datetime-local",
                'class': 'form-control',
                'placeholder': 'Дата и время создания'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание прогноза'
            })
        }