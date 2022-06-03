from django.contrib import admin
from .models import AAAData, XYZData


class ModelAAAData(admin.ModelAdmin):
    list_display = ('id', 'addload', )
    list_display_links = ('id', 'addload',)
    list_filter = ('id',)
    ordering = ('id',)


class ModelXYZData(admin.ModelAdmin):
    list_display = ('id', 'x', 'y', 'z',)
    list_display_links = ('id', 'x', 'y', 'z',)
    list_filter = ('id',)
    ordering = ('id',)


admin.site.register(AAAData, ModelAAAData)
admin.site.register(XYZData, ModelXYZData)

