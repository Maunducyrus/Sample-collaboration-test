from django.contrib import admin
from .models import Inventory, Sale, Order

# Register your models here.
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'reorder_level', 'expiry_date', 'price_per_unit')

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('inventory_item', 'quantity_sold', 'amount', 'date')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('inventory_item', 'quantity_ordered', 'order_date', 'status')
