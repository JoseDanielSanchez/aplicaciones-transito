from django.contrib import admin

# Register your models here.
from .models import ReporteTransito

class ReporteTransitoAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_per_page = 20
    list_display = ['id','fecha','tipo','descripcion','latitud','longitud',"usuario_id"]

admin.site.register(ReporteTransito,ReporteTransitoAdmin)