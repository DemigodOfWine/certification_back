from django.db import models
from .mModel import Model
from .mSettings1560 import Settings1560
from .mOperators import Operators
from .mControllers import Controllers
from .mRanges import Ranges
from .mBase import Base
from .formOne import FormOne
from .formTwo import FormTwo
from .formForAll import FormForAll
from django.contrib.postgres.fields import ArrayField


class Certification(FormForAll, FormOne, FormTwo):

    class VerificationStage(models.IntegerChoices):
        IDX_1 = 0, 'Первичная'
        IDX_2 = 1, 'Вторичная'

    model = models.ForeignKey(Model, on_delete=models.CASCADE, default=None, verbose_name="Модель",
                              related_name='model_certification')
    operator = models.ForeignKey(Operators, on_delete=models.CASCADE, default=None, verbose_name="Оператор",
                                    related_name='operator')
    controller = models.ForeignKey(Controllers, on_delete=models.CASCADE, default=None, verbose_name="Контроллер",
                                    related_name='controller')
    settings = models.ForeignKey(Settings1560, on_delete=models.CASCADE, default=None, verbose_name="Настройки А1560",
                                    related_name='settings')
    ranges = models.ForeignKey(Ranges, on_delete=models.CASCADE, default=None, null=True, verbose_name="Допуски",
                                  related_name='ranges')
    base = models.ForeignKey(Base, on_delete=models.CASCADE, default=None, verbose_name="Базовые х-ки",
                                    related_name='base')
    serial_number = models.CharField(max_length=16)
    temp = models.DecimalField(max_digits=4, decimal_places=2, default=None, null=True, verbose_name="Температура, С")
    humid = models.DecimalField(max_digits=4, decimal_places=2, default=None, null=True, verbose_name="Влажность, отн.")
    verification_stage = models.IntegerField(choices=VerificationStage.choices, default=None,
                                             verbose_name="Этап контроля")
    comment = models.TextField(max_length=500, null=True, blank=True, verbose_name="Комментарий")
    date_time = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Дата внесения записи")
    result = models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], null=True, default=False,
                                 verbose_name="Результат")
    ascan = ArrayField(models.DecimalField(max_digits=15, decimal_places=10, default=None, null=True), default=None)

    dmg = models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], null=True, default=False,
                              verbose_name="Списание")
    serial_number_b = models.CharField(max_length=16, null=True, default=None, blank=True,
                                       verbose_name="Базовый серийный номер")
    phase_wave = models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], null=True, default=True,
                                 verbose_name="Фаза первой полуволны")
    assembled = models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], null=True, default=True,
                                 verbose_name="В сборке")
    # insulation = ArrayField(models.DecimalField(max_digits=15, decimal_places=10, default=None, null=True),
    #                                default=None)

    manager = models.Manager()

    class Meta:
        db_table = "dpc_certification"
        app_label = "cap_server"
        verbose_name = "Результаты паспортизации"
        verbose_name_plural = "Результаты паспортизации"

    def __str__(self):
        return str(self.model)
