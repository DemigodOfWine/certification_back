from django import forms
from django.core import validators
from ..models import Model, Certification


class SearchCertificate(forms.Form):
    VERIFICATION_CHOICES = Certification.VerificationStage.choices

    model = forms.ModelChoiceField(queryset=Model.manager.all().order_by('model_name'))
    serialNumberDown = forms.CharField(label='Серийный номер от', max_length=7,
                                       validators=[validators.RegexValidator(
                                           regex='^[A-Z,a-z][0-9]{3}$|^[0-9]{6}$|^[0-9]{7}$')],
                                       error_messages={'invalid': 'Ошибка в номере'})
    serialNumberUp = forms.CharField(label='Серийный номер до', max_length=7,
                                     validators=[validators.RegexValidator(
                                         regex='^[A-Z,a-z][0-9]{3}$|^[0-9]{6}$|^[0-9]{7}$')],
                                     error_messages={'invalid': 'Ошибка в номере'})
    result = forms.BooleanField(required=False)
    date_time_first = forms.DateTimeField(initial=Certification.manager.first().date_time)
    date_time_last = forms.DateTimeField(initial=Certification.manager.last().date_time)
    verification = forms.MultipleChoiceField(choices=VERIFICATION_CHOICES)
