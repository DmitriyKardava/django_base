from django.contrib import admin
from authapp.models import ShopUser

# Register your models here.


@admin.register(ShopUser)
class ShopUserAdmin(admin.ModelAdmin):
    pass
