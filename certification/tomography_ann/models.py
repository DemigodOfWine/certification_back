from django.db import models


class AAAData(models.Model):
    addload = models.IntegerField(null=True)
    bcd = models.JSONField(null=True, blank=True)
    xm = models.IntegerField(null=True, blank=True)
    ym = models.IntegerField(null=True, blank=True)
    zm = models.IntegerField(null=True, blank=True)
    idxDualAR = models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], null=True, default=False, blank=True)
    idxSingleARposition = models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], null=True, default=False, blank=True)
    weldparam = models.JSONField(null=True, blank=True)
    poroglvl = models.IntegerField(null=True, blank=True)
    levelfix = models.DecimalField(max_digits=4, decimal_places=2, default=None, null=True, blank=True)
    bcdl = models.JSONField(null=True, blank=True)
    bcdr = models.JSONField(null=True, blank=True)
    stpY = models.IntegerField(null=True, blank=True)
    wa = models.IntegerField(null=True, blank=True)
    alimin = models.IntegerField(null=True, blank=True)
    alimax = models.IntegerField(null=True, blank=True)
    balance = models.IntegerField(null=True, blank=True)
    dxn = models.IntegerField(null=True, blank=True)
    cscan = models.JSONField(null=True, blank=True)
    amaxC = models.IntegerField(null=True, blank=True)
    amaxD = models.IntegerField(null=True, blank=True)
    dydsize = models.IntegerField(null=True, blank=True)
    bscan = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = 'aaa_data'
        verbose_name = "Сырой сигнал"
        verbose_name_plural = "Сырой сигнал"


class XYZData(models.Model):

    class Defect(models.IntegerChoices):
        IDX_1 = 0, 'Плоскостной'
        IDX_2 = 1, 'Объемный'
        IDX_3 = 3, 'Объемно-плоскостной'

    result = models.ForeignKey(AAAData, on_delete=models.CASCADE, default=None)
    x = models.IntegerField(null=True)
    y = models.IntegerField(null=True)
    z = models.IntegerField(null=True)
    dx = models.IntegerField(null=True)
    dy = models.IntegerField(null=True)
    dz = models.IntegerField(null=True)
    a = models.IntegerField(null=True)
    da = models.IntegerField(null=True)
    typy_defect = models.IntegerField(choices=Defect.choices, default=None, verbose_name="Дефект")

    class Meta:
        db_table = 'xyz_data'
        verbose_name = "Дефект"
        verbose_name_plural = "Дефекты"
