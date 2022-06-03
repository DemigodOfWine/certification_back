from django.db import models


class FormTwo(models.Model):

    afc_maximum_s_rel_first_half_wave = models.DecimalField(max_digits=10, decimal_places=5, default=None, null=True,
                                                            blank=True, verbose_name=
                                                            "Коэффициент двойного преобразования по первой полуволне (не менее), дБ")
    leading_front_duration = models.DecimalField(max_digits=10, decimal_places=5, default=None, null=True, blank=True,
                                                   verbose_name="Длительность фронта первой полуволны, мкс")
    first_half_wave_duration = models.DecimalField(max_digits=10, decimal_places=5, default=None, null=True, blank=True,
                                                           verbose_name="Длительность первой полуволны, мкс")
    afc_frequency_maximum_first_wave = models.DecimalField(max_digits=10, decimal_places=5, default=None, null=True,
                                                           blank=True, verbose_name=
                                                           "Частота максимума АЧХ по первому периоду, кГц")

    class Meta:
        abstract = True
