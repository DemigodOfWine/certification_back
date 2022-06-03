from django.db import models


class FormForAll(models.Model):

    echo_pulse_delay = models.DecimalField(max_digits=10, decimal_places=5, default=None, null=True, blank=True,
                                                   verbose_name="Задержка сигнала, мкс")
    capacity = models.DecimalField(max_digits=10, decimal_places=5, default=None, null=True, blank=True,
                                   verbose_name="Емкость, пФ")

    class Meta:
        abstract = True
