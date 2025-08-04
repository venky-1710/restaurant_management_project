
from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_amount', 'status', 'ordered_at')
    list_filter = ('status', 'ordered_at')
    search_fields = ('customer__username',)
    filter_horizontal = ('order_items',)