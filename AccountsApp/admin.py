from django.contrib import admin
from .models import CustomUser as User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username',]
    list_per_page = 30
admin.site.register(User, UserAdmin)
