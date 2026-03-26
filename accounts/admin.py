from django.contrib import admin
from .models import CRMProfile


@admin.register(CRMProfile)
class CRMProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'corporate_email')
    search_fields = ('user__username', 'corporate_email')