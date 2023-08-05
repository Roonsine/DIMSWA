from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group

admin.site.site_header = 'Synyster Studios'


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'product_id',
        'cost',
        'category',
        'quantity'
    )
    list_filter = ['product_id', 'name']


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
# admin.site.unregister(Group)
