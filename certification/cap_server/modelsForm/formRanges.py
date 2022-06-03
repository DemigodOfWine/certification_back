from ..models import Ranges
from django.forms import ModelForm


class FormRanges(ModelForm):
    class Meta:
        model = Ranges
        fields = ['model',
                  'afc_maximum_s_rel', 'echo_pulse_duration', 'afc_frequency_maximum',
                  'lower_afc_frequency', 'upper_afc_frequency', 'operating_frequency',
                  'relative_transmission_bandwidth', 'capacity', 'echo_pulse_delay',
                  'afc_frequency_maximum_first_wave',
                  'afc_maximum_s_rel_first_half_wave', 'first_half_wave_duration',
                  'leading_front_duration', 'comment']




