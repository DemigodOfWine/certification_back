from django.db import models


class DefectPEP(models.Model):
    defect = models.CharField(max_length=50, default=None)

    class Meta:
        db_table = "pep_defect"
        app_label = "pep_server"
        verbose_name = "Дефекты ПЭП"
        verbose_name_plural = "Дефекты ПЭП"

    def __str__(self):
        return self.defect






