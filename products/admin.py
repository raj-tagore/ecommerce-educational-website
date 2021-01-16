from django.contrib import admin
from .models import Product, Buyer


# Register your models here.
class ProductTable(admin.ModelAdmin):
    list_display= ('Name', 'Price', 'DiscountedPrice', 'ActivateDiscount', 'Display', 'Position', 'id')
admin.site.register(Product, ProductTable)

class BuyerTable(admin.ModelAdmin):
    list_display= ('Name', 'ProductName', 'Phone', 'Email', 'id')
admin.site.register(Buyer, BuyerTable)

