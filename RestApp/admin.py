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

class ChefAdmin(admin.ModelAdmin):
    list_display = ['chef_name', 'gender', 'active', 'mobile']
    list_per_page = 50
    list_editable = ['active']
admin.site.register(Chef, ChefAdmin)

class AllocationAdmin(admin.ModelAdmin):
    list_display = ['id' ,'orderitem_id', 'orderitem_name', 'orderitem_category', 'quantity', 'chef', 'status']
    list_per_page = 50
    list_editable = ['status',]
admin.site.register(Allocation, AllocationAdmin)