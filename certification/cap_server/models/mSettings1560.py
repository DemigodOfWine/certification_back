from .settings1560 import AbstractSettings1560
from .mModel import Model
from django.db import models


class Settings1560(AbstractSettings1560):

    model = models.ForeignKey(Model, on_delete=models.CASCADE, verbose_name="Модель")
    echo_pulse_delay_receiver = models.DecimalField(max_digits=4, decimal_places=2, default=None, null=True,
                                                    verbose_name="Задержка приемного тракта, мкс")

    class Meta:
        db_table = "dpc_settings1560"
        app_label = "cap_server"
        verbose_name = "Настройки А1560"
        verbose_name_plural = "Настройки А1560"

    def __str__(self):
        return str(self.model)
