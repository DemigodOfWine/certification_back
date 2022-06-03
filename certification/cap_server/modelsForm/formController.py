from ..models import Controllers
from django.forms import ModelForm


class FormController(ModelForm):
    class Meta:
        model = Controllers
        fields = ['login', 'name_rus', 'name_eng', 'status']
