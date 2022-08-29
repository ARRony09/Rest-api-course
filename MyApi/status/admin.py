from pyexpat import model
from django.contrib import admin
from .models import StatusModel
# Register your models here.


class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'image']

    class Meta:
        model = StatusModel


admin.site.register(StatusModel, StatusAdmin)
