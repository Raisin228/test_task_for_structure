from django.contrib import admin
from .models import AnyFile


class AnyFileDisplayOnAdminPanel(admin.ModelAdmin):
    """Form for the admin panel (displayed fields)"""
    list_display = ['some_name', 'url_image', 'url_file']


admin.site.register(AnyFile, AnyFileDisplayOnAdminPanel)
