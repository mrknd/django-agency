from django.contrib import admin
from .models import Case


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'country', 'is_published', 'created_at')
    list_filter = ('is_published', 'category', 'country')
    search_fields = ('title', 'short_description', 'task', 'result')
    prepopulated_fields = {'slug': ('title',)}