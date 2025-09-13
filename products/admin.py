from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import (
    Product, Unit, Category, Brand, Warranty,
    SellingPriceGroup, Variation, BranchProductStock
)

@admin.register(Unit)
class UnitAdmin(ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Brand)
class BrandAdmin(ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Warranty)
class WarrantyAdmin(ModelAdmin):
    list_display = ['name', 'duration', 'duration_type']
    search_fields = ['name']
    list_filter = ['duration_type']

@admin.register(SellingPriceGroup)
class SellingPriceGroupAdmin(ModelAdmin):
    list_display = ['name', 'price_multiplier']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['name', 'sku', 'unit_name', 'category_name', 'brand_name', 'warranty_name']
    search_fields = ['name', 'sku']
    list_filter = ['unit_name', 'category_name', 'brand_name']

@admin.register(Variation)
class VariationAdmin(ModelAdmin):
    list_display = ['name', 'sku_suffix', 'product_name']
    search_fields = ['name', 'sku_suffix']
    list_filter = ['product_name']

@admin.register(BranchProductStock)
class BranchProductStockAdmin(ModelAdmin):
    list_display = ['product_name', 'branch_name', 'quantity', 'opening_stock']
    search_fields = ['product_name__name', 'branch_name__name']
    list_filter = ['branch_name']
