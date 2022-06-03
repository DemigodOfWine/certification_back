from django.db import models


class FormOne(models.Model):

    afc_maximum_s_rel = models.DecimalField(max_digits=10, decimal_places=5, default=None, null=True, blank=True,
                                                    verbose_name="Коэффициент двойного преобразования (не менее), дБ")
    echo_pulse_duration = models.DecimalField(max_digits=10, decimal_places=5, default=None, null=True, blank=True,
                                                      verbose_name="Длительность сигнала, мкс")
    afc_frequency_maximum = models.DecimalField(max_digits=10, decimal_places=5, default=None, null=True, blank=True,
                                                        verbose_name="Частота максимума АЧХ, кГц")
    lower_afc_frequency = models.DecimalField(max_digits=10, decimal_places=5, default=None, null=True, blank=True,
                                                      verbose_name="Нижняя граничная частота АЧХ, кГц")
    upper_afc_frequency = models.DecimalField(max_digits=10, decimal_places=5, default=None, null=True, blank=True,
                                                      verbose_name="Верхняя граничная частота АЧХ, кГц")
    operating_frequency = models.DecimalField(max_digits=10, decimal_places=5, default=None, null=True, blank=True,
                                                      verbose_name="Рабочая частота, кГц")
    relative_transmission_bandwidth = models.DecimalField(max_digits=10, decimal_places=5, default=None, null=True,
                                                          blank=True, verbose_name="Относительная полоса АЧХ, %")

    class Meta:
        abstract = True
