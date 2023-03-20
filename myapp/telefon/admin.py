from django.contrib import admin
from .models import Phones, Brand, Electronic

# Register your models here.
class PhonesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'color', 'electronic')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Phones, PhonesAdmin)
admin.site.register(Brand)
admin.site.register(Electronic)