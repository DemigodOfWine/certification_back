from .userCertification import UserCertification
from django.contrib.auth.models import User
from django.db import models
from .mControllers import Controllers


class Operators(UserCertification):

    class VerificationLevel(models.IntegerChoices):
        IDX_1 = 0, 'Первичный контроль'
        IDX_2 = 1, 'Контроль качества'

    login = models.OneToOneField(User, on_delete=models.CASCADE)
    controlers_of_operator = models.ManyToManyField(Controllers, verbose_name="Контролеры")
    password = models.CharField(max_length=50, default=None, null=True, blank=True,)
    verification_level = models.IntegerField(choices=VerificationLevel.choices, default=None, null=True, blank=True,
                                             verbose_name="Этап контроля")

    manager = models.Manager()

    class Meta:
        db_table = "dpc_operators"
        app_label = "cap_server"
        verbose_name = "Оператор"
        verbose_name_plural = "Операторы"

    def __str__(self):
        return str(self.login)
