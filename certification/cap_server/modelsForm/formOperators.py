from django import forms
from ..models import Operators
from django.forms import ModelForm


class FormOperators(ModelForm):
    class Meta:
        model = Operators
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['login', 'name_rus', 'name_eng', 'status', 'verification_level', 'controlers_of_operator', 'password']
