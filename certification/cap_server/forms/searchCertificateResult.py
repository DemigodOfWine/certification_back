from django.forms import ModelForm
from ..models import Certification


class SearchCertificateResult(ModelForm):

    class Meta:
        model = Certification
        fields = ['serial_number', 'humid', 'temp', 'afc_frequency_maximum']
