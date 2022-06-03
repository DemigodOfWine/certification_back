from django.db import models


class ModelPEP(models.Model):

    model_name = models.CharField(max_length=10, unique=True, verbose_name="Модель")
    manager = models.Manager()

    class Meta:
        db_table = "pep_model"
        app_label = "pep_server"
        verbose_name = "Модели ПЭП"
        verbose_name_plural = "Модели ПЭП"

    def __str__(self):
        return self.model_name






