from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

from .modelsForm import FormController, FormOperators, FormSettings, FormBase, FormRanges
from django.contrib import admin
from .models import Model, Base, Certification, Ranges, Operators, Controllers, Settings1560


class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_name', 'model_b', 'status', 'application', 'form_certificate', 'intended_use_rus',
                    'photo', 'image_img', 'model_postfix')
    list_display_links = ('id', 'model_name',)
    list_filter = ('form_certificate', 'status',)
    ordering = ('model_name',)
    readonly_fields = ('image_img',)


class RangesAdmin(admin.ModelAdmin):
    list_display = ('model', 'afc_maximum_s_rel', 'afc_maximum_s_rel_first_half_wave',)
    form = FormRanges
    ordering = ('model',)


class SettingsAdmin(admin.ModelAdmin):
    form = FormSettings
    list_display = ('model', 'sampling_frequency', 'zonder_frequency', 'zonder_periods', 'zonder_amplitude',)
    list_display_links = ('model',)
    list_filter = ('zonder_frequency',)
    ordering = ('model',)


class CertificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'serial_number', 'serial_number_b', 'assembled', 'dmg', 'date_time',
                    'afc_frequency_maximum', 'afc_frequency_maximum_first_wave',
                    'afc_maximum_s_rel', 'afc_maximum_s_rel_first_half_wave', 'dmg', 'serial_number_b',)
    list_display_links = ('model', 'serial_number',)
    list_filter = ('model', ('date_time', DateRangeFilter), 'date_time', 'result',
                   'verification_stage', 'dmg',)
    search_fields = ['serial_number']


class BaseAdmin(admin.ModelAdmin):
    list_display = ('model', 'afc_maximum_s_rel', 'echo_pulse_duration', 'afc_frequency_maximum',
                    'lower_afc_frequency', 'upper_afc_frequency', 'operating_frequency',)
    list_display_links = ('model',)
    form = FormBase
    ordering = ('model',)


class ControllersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_rus', 'login', 'status', 'name_eng')
    list_display_links = ('id', 'name_rus', 'login')
    list_filter = ('status',)
    form = FormController


class OperatorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_rus', 'login', 'status', 'name_eng', 'verification_level')
    list_display_links = ('id', 'name_rus', 'login')
    list_filter = ('status',)
    form = FormOperators


admin.site.register(Model, ModelAdmin)
admin.site.register(Base, BaseAdmin)
admin.site.register(Settings1560, SettingsAdmin)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(Ranges, RangesAdmin)
admin.site.register(Operators, OperatorsAdmin)
admin.site.register(Controllers, ControllersAdmin)


