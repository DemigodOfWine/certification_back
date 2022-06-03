from django.db import models


class AbstractSettings1560(models.Model):

    GAIN_RAW = (
        ("0 0 0", "0/0/0"),
        ("0 0 1", "0/0/1"),
        ("0 1 0", "0/1/0"),
        ("1 0 0", "1/0/0"),
        ("0 1 1", "0/1/1"),
        ("1 0 1", "1/0/1"),
        ("1 1 0", "1/1/0"),
        ("1 1 1", "1/1/1"),
    )

    TVG_MODE = (
        ("ON", "ON"),
        ("BYPASS", "BYPASS"),
    )

    SOURCE_SYNC = (
        ("CTP", "CTP"),
        ("SENSOR", "SENSOR"),
        ("INTERNAL", "INTERNAL"),
    )

    ON_OFF = (
        ("ON", "ON"),
        ("OFF", "OFF"),
    )

    ZONDER_MODE = (
        ("COMBINED", "COMBINED"),
        ("SPLIT", "SPLIT"),
    )

    class FilterIndex(models.IntegerChoices):
        HPF_10 = 0, '10 kHz'
        HPF_20 = 1, '20 kHz'
        HPF_40 = 2, '40 kHz'
        HPF10_BYPASS = 3, 'BYPASS'

    class ZonderAmplitude(models.IntegerChoices):
        ZA_50 = 50, '50'
        ZA_100 = 100, '100'
        ZA_200 = 200, '200'

    class EmuData(models.IntegerChoices):
        EMU_DATA_OFF = 0, 'OFF'
        EMU_DATA_ON = 1, 'ON'

    start_signal = models.DecimalField(max_digits=5, decimal_places=1, default=None, verbose_name="Начало сигнала, мкс")
    end_signal = models.DecimalField(max_digits=5, decimal_places=1, default=None, verbose_name="Конец сигнала, мкс")
    end_draw_signal = models.DecimalField(max_digits=5, decimal_places=1, default=None,
                                          verbose_name="Конец отрисовки сигнала, мкс")
    gain_raw = models.CharField(max_length=6, choices=GAIN_RAW, verbose_name="GAIN RAW(аттенюатора/3 каскад/2 каскад)")
    tvg_mod = models.CharField(max_length=6, choices=TVG_MODE, verbose_name="TVG MODE")
    tvg_atten = models.BooleanField(choices=[(True, 'on'), (False, 'off')], default=False, verbose_name="Аттенюатор")
    tvg_K3 = models.BooleanField(choices=[(True, 'on'), (False, 'off')], default=False, verbose_name="3 каскад")
    tvg_K2 = models.BooleanField(choices=[(True, 'on'), (False, 'off')], default=False, verbose_name="2 каскад")
    tvg_bypass = models.DecimalField(max_digits=5, decimal_places=1, default=None, verbose_name="Усиление, дБ")
    source_sync = models.CharField(max_length=20, choices=SOURCE_SYNC, verbose_name="Источник синхронизации")
    accumulation = models.PositiveIntegerField(verbose_name="Накопление")
    filter_index = models.IntegerField(choices=FilterIndex.choices, default=None, verbose_name="Фильтр")
    ascan_lenght = models.PositiveIntegerField(verbose_name="Длина вектора ASCAN")
    constant_delay = models.PositiveIntegerField(verbose_name="Интервал постоянной задержки начала зондирования")
    random_delay = models.PositiveIntegerField(verbose_name="Диапазон значений случайной задержки начала зондирования")
    sampling_frequency = models.PositiveIntegerField(
        verbose_name="Частота квантования, МГц")
    zonder_frequency = models.PositiveIntegerField(verbose_name="Частота зондера, Гц")
    zonder_periods = models.DecimalField(max_digits=5, decimal_places=1, default=None,
                                         verbose_name="Число периодов зондера")
    zonder_amplitude = models.IntegerField(choices=ZonderAmplitude.choices, default=None,
                                           verbose_name="Амплитуда зондера, В")
    zonder_enable = models.CharField(max_length=3, choices=ON_OFF, verbose_name="ZONDER ENABLE")
    zonder_reverse_polarity = models.CharField(max_length=3, choices=ON_OFF,
                                               verbose_name="Реверсирование полярности")
    zonder_mode = models.CharField(max_length=10, choices=ZONDER_MODE,
                                               verbose_name="ZONDER_MODE")
    damp_duration = models.PositiveIntegerField(verbose_name="Интервал дампирования")
    emu_data = models.IntegerField(choices=EmuData.choices, default=None, verbose_name="Эмуляция данных")

    class Meta:
        abstract = True
