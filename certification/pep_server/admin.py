from django.contrib import admin
from .models import ModelPEP, DefectPEP, BasePEP


class ModelPEPAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_name',)
    list_display_links = ('id', 'model_name',)
    ordering = ('model_name',)


class BasePEPAdmin(admin.ModelAdmin):
    list_display = ('model', 'postfix',)
    list_display_links = ('model', 'postfix',)
    ordering = ('postfix',)


class DefectPEPAdmin(admin.ModelAdmin):
    list_display = ('id', 'defect',)
    list_display_links = ('id', 'defect',)
    ordering = ('id',)


admin.site.register(ModelPEP, ModelPEPAdmin)
admin.site.register(DefectPEP, DefectPEPAdmin)
admin.site.register(BasePEP, BasePEPAdmin)
