from django.db import models
from .ModelPEP import ModelPEP


class BasePEP(models.Model):

    model = models.ForeignKey(ModelPEP, on_delete=models.CASCADE, verbose_name="Модель")
    postfix = models.CharField(max_length=15, unique=True, verbose_name="Постфикс")
    manager = models.Manager()

    class Meta:
        db_table = "pep_base"
        app_label = "pep_server"
        verbose_name = "Базовые х-ки ПЭП"
        verbose_name_plural = "Базовые х-ки ПЭП"

    def __str__(self):
        return self.postfix






