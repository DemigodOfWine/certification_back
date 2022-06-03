from django.db import models


class UserCertification(models.Model):

    name_rus = models.CharField(max_length=150, null=True, blank=True)
    name_eng = models.CharField(max_length=150, null=True, blank=True)
    status = models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')],
                                 default=None, verbose_name="Администратор")

    class Meta:
        abstract = True
