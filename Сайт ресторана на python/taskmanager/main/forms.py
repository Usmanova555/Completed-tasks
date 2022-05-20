from django.core.exceptions import ValidationError

from .models import *
from django.forms import ModelForm, TextInput, Textarea
from django.forms import forms


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ["title", "time_from", "time_to", "phone_number", "number_of_table"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Ваше ФИО:'
            }),
            "time_from": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дату и время от начала бронирования'
            }),
            "time_to": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дату и время до окончания бронирования'
            }),
            "phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ввредите Ваш номер телефона:'
            }),
            "number_of_table": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ввредите номер столика от 1 до 14'
            })
        }


class ForumForm(ModelForm):
    class Meta:
        model = Forum
        fields = ['title_fio', "message", 'image']
        widgets = {
            "title_fio": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Ваше ФИО:'
            }),
            "message": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст отзыва:'
            })
        }

    def clean_title_fio(self):
        title_fio = self.cleaned_data['title_fio']
        if len(title_fio) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title_fio


class WorkForm(ModelForm):
    class Meta:
        model = Work
        fields = ["title", "name_of_work", "text", "age"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Ваше ФИО:'
            }),
            "name_of_work": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Выбранное Вами поле деятельности:'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше резюме (опишите опыт и причины)'
            }),
            "age": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сколько Вам лет?'
            })
        }


class NewForm(ModelForm):
    class Meta:
        model = New
        fields = ["title", "phone_number", "name"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Ваше ФИО:'
            }),
            "phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Ваш номер телефона:'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название блюда:'
            })
        }

