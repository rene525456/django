from django.contrib import admin
from .models import CentroComercial, CategoriaLocal, Local

class CentroComercialAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['id','name']
    search_fields = ['name']
    list_per_page = 10

class LocalAdmin(admin.ModelAdmin):
    list_display = ['id','name','centro_comercial']
    list_display_links = ['name','centro_comercial']
    search_fields = ['name']
    list_filter = [ 'name']
    list_per_page = 10

class CategoriaLocalAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['name']
    list_per_page = 10

admin.site.register(CentroComercial, CentroComercialAdmin)
admin.site.register(Local, LocalAdmin)
admin.site.register(CategoriaLocal, CategoriaLocalAdmin)
