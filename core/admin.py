from django.contrib import admin
from .models import Case, BlogPost, Contacts


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'country', 'is_published', 'created_at')
    list_filter = ('is_published', 'category', 'country')
    search_fields = ('title', 'short_description', 'task', 'result')
    prepopulated_fields = {'slug': ('title',)}



@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'published_at')
    list_filter = ('category', 'is_published', 'published_at')
    prepopulated_fields = {}
    search_fields = ('title', 'excerpt', 'content')


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return not Contacts.objects.exists()