from django.contrib import admin
from .models import Publication 

# Register your models here.
class PublicationAdmin (admin.ModelAdmin):
    list_display = ('title', 'author__username', 'date', 'updated')
    list_filter = ('author', 'date', 'updated')
    search_fields = ('title', 'body', 'author__username')
    ordering = ('date',)

admin.site.register(Publication, PublicationAdmin)