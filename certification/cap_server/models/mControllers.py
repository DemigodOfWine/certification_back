from .userCertification import UserCertification
from django.contrib.auth.models import User
from django.db import models


class Controllers(UserCertification):

    login = models.OneToOneField(User, on_delete=models.CASCADE)

    manager = models.Manager()

    class Meta:
        db_table = "dpc_controller"
        app_label = "cap_server"
        verbose_name = "Контролер"
        verbose_name_plural = "Контролеры"

    def __str__(self):
        return str(self.login)
