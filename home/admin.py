
from django.contrib import admin
from .models import Menu
from .models import Restaurant

admin.site.register(Restaurant)
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)