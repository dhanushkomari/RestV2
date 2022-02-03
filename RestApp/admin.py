from django.contrib import admin
from .models import OrderItem, Chef, Category, Allocation

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'category_name']
    list_per_page = 30
admin.site.register(Category, CategoryAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'orderitem_id', 'category_id', 'category_name', 'product_id', 'product_name', 'table_no', 'quantity', 'allocated']
    list_per_page = 30
    list_editable = ['allocated']
admin.site.register(OrderItem, OrderItemAdmin)


admin.site.register(Chef)

class AllocationAdmin(admin.ModelAdmin):
    list_display = ['orderitem_id', 'orderitem_name', 'orderitem_category', 'quantity', 'chef']
    list_per_page = 50
admin.site.register(Allocation, AllocationAdmin)