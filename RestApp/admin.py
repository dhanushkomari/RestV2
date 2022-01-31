from django.contrib import admin
from .models import OrderItem, Chef, Category, Allocation

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'category_name']
    list_per_page = 30
admin.site.register(Category, CategoryAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'orderitem_id', 'category_id', 'category_name', 'product_id', 'product_name', 'table_no', 'quantity']
    list_per_page = 30
admin.site.register(OrderItem, OrderItemAdmin)


admin.site.register(Chef)
admin.site.register(Allocation)