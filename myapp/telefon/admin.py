from django.contrib import admin
from .models import Phones, Brand, Electronic

# Register your models here.
class PhonesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'color', 'published', 'types')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Phones, PhonesAdmin)
admin.site.register(Brand)
admin.site.register(Electronic)