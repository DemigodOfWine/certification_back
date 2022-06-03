from ..models import Base
from django.forms import ModelForm


class FormBase(ModelForm):
    class Meta:
        model = Base
        fields = ['model', 'special_properties',
                  'apyas', 'control_line', 'zonder_line', 'capacity_line', 'acoustic_insulation_line', 'wave_type',
                  'damper', 'phase', 'maximum_excitation_pulse_voltage', 'height', 'diameter',
                  'weight', 'connector', 'temp_down', 'temp_up',
                  'echo_pulse_delay', 'capacity',
                  'afc_maximum_s_rel', 'echo_pulse_duration', 'afc_frequency_maximum',
                  'lower_afc_frequency', 'upper_afc_frequency', 'operating_frequency',
                  'relative_transmission_bandwidth', 'afc_maximum_s_rel_first_half_wave', 'leading_front_duration',
                  'first_half_wave_duration', 'afc_frequency_maximum_first_wave', 'comment']




