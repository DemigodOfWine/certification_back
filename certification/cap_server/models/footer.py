from django.db import models


class Footer(models.Model):

    date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Дата внесения записи")
    last_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Последние изменение")
    comment = models.TextField(max_length=500, null=True, blank=True, verbose_name="Комментарий")

    class Meta:
        abstract = True
