from django.db import models


class Model(models.Model):

    class Format(models.IntegerChoices):
        DAMPER = 1, 'Демпфированные'
        NO_DAMPER = 2, 'Не демпфированные'

    model_name = models.CharField(max_length=10, unique=True, verbose_name="Модель")
    photo = models.ImageField(upload_to='dpc/img/', null=True)
    form_certificate = models.IntegerField(choices=Format.choices, null=True, verbose_name="Форма паспорта")
    intended_use_rus = models.TextField(max_length=500, verbose_name="Назначение", null=True, default=None, blank=True)
    intended_use_eng = models.TextField(max_length=500, verbose_name="Назначение", null=True, default=None, blank=True)
    application = models.TextField(max_length=500, verbose_name="Применение", null=True, default=None,
                                    blank=True)
    status = models.CharField(max_length=2, null=True, choices=[("С", "Капсула"), ("S", "Преобразователь")],
                                 verbose_name="Вид изделия")
    model_b = models.ForeignKey('self', default=None, on_delete=models.CASCADE, blank=True, null=True,
                                verbose_name="Базовая капсула")
    model_postfix = models.CharField(max_length=20, verbose_name="Постфикс", null=True, default=None, blank=True)

    manager = models.Manager()

    class Meta:
        db_table = "dpc_model"
        app_label = "cap_server"
        verbose_name = "Модели преобразователей"
        verbose_name_plural = "Модели преобразователей"

    def __str__(self):
        return self.model_name

    def image_img(self):
        if self.photo:
            return u'<img src="%s"/>' % self.photo.url
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True





