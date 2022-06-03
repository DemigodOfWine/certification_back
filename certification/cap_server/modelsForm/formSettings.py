from ..models import Settings1560
from ..models import AbstractSettings1560
from django.forms import ModelForm


class FormSettings(ModelForm):
    class Meta:
        model = Settings1560
        fields = ['model', 'start_signal', 'end_signal',
                  'end_draw_signal', 'gain_raw', 'tvg_mod', 'tvg_atten', 'tvg_K3', 'tvg_K2',
                  'tvg_bypass', 'source_sync', 'accumulation',
                  'filter_index', 'ascan_lenght', 'constant_delay',
                  'random_delay', 'sampling_frequency', 'zonder_frequency',
                  'zonder_periods', 'zonder_amplitude', 'zonder_enable',
                  'zonder_reverse_polarity', 'zonder_mode', 'damp_duration',
                  'emu_data', 'echo_pulse_delay_receiver']




