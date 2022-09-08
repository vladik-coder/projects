from django.contrib import admin

from .models import*

class KazanAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'price_new', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'id')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'volume')

admin.site.register(Kazan, KazanAdmin)

