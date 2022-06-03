from django.db import models
from .mModel import Model
from .formForAll import FormForAll
from .formOne import FormOne
from .formTwo import FormTwo
from .footer import Footer


class Base(FormForAll, FormOne, FormTwo, Footer):

    model = models.ForeignKey(Model, on_delete=models.CASCADE, default=None, verbose_name="Модель",
                                    related_name='model_base')
    special_properties = models.CharField(max_length=200, null=True, verbose_name="Особые свойства", blank=True)
    apyas = models.CharField(max_length=16, null=True, default=None, verbose_name="АПЯС")
    control_line = models.PositiveIntegerField(default=None, null=True, verbose_name="Канал контроля")
    zonder_line = models.PositiveIntegerField(default=None, null=True, verbose_name="Канал зондера")
    capacity_line = models.PositiveIntegerField(default=None, null=True, verbose_name="Канал емкости")
    acoustic_insulation_line = models.PositiveIntegerField(default=None, null=True,
                                                           verbose_name="Канал акустической изоляции")
    maximum_excitation_pulse_voltage = models.DecimalField(max_digits=5, decimal_places=1, default=None, null=True,
                                  verbose_name="Максимальная амплитуда возбуждения, В")
    wave_type = models.CharField(max_length=2, null=True, choices=[("sh", "Поперечные"), ("l", "Продольные")],
                                     verbose_name="Основной тип возбуждаемых волн")
    damper = models.BooleanField(choices=[(True, 'Есть'), (False, 'Нет')], default=False, null=True,
                                 verbose_name="Демпфер")
    phase = models.BooleanField(choices=[(True, 'Положительная'), (False, 'Отрицательная')], null=True, default=False,
                                verbose_name="Первая полуволна")
    height = models.DecimalField(max_digits=4, decimal_places=2, default=None, null=True, verbose_name="Высота, мм")
    diameter = models.DecimalField(max_digits=4, decimal_places=2, default=None, null=True, verbose_name="Диаметр, мм")
    weight = models.DecimalField(max_digits=4, decimal_places=2, default=None, null=True, verbose_name="Масса, г")
    connector = models.CharField(max_length=16, null=True, default=None, verbose_name="Тип разъема")
    temp_down = models.DecimalField(max_digits=4, decimal_places=2, default=None, null=True,
                                    verbose_name="Нижний диапазон рабочей температуры, С")
    temp_up = models.DecimalField(max_digits=4, decimal_places=2, default=None, null=True,
                                  verbose_name="Верхний диапазон рабочей температуры, С")

    manager = models.Manager()

    class Meta:
        db_table = 'dpc_base'
        app_label = "cap_server"
        verbose_name = "Базовые характеристики"
        verbose_name_plural = "Базовые характеристики"

    def __str__(self):
        return str(self.model)
