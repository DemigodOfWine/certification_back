from django.db import models
from .mModel import Model
from .footer import Footer
from .formOne import FormOne
from .formTwo import FormTwo
from .formForAll import FormForAll


class Ranges(FormOne, FormTwo, FormForAll, Footer):

    model = models.ForeignKey(Model, on_delete=models.CASCADE, verbose_name="Модель")

    manager = models.Manager()

    class Meta:
        db_table = "dpc_ranges"
        app_label = "cap_server"
        verbose_name = "Допуски"
        verbose_name_plural = "Допуски"

    def __str__(self):
        return str(self.model)
