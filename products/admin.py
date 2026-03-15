from django.contrib import admin
from .models import Product, Category, ProductVariant


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 3
    fields = ['size', 'color', 'color_hex', 'sku', 'stock', 'pod_variant_id']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'is_active', 'is_featured', 'created_at']
    list_filter = ['category', 'is_active', 'is_featured']
    list_editable = ['is_active', 'is_featured', 'price', 'stock']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductVariantInline]
    fieldsets = (
        ('Basic Info', {'fields': ('name', 'slug', 'category', 'description')}),
        ('Pricing', {'fields': ('price', 'compare_price')}),
        ('Images', {'fields': ('image', 'image2', 'image3')}),
        ('Inventory', {'fields': ('stock', 'is_active', 'is_featured')}),
        ('POD Integration', {'fields': ('pod_provider', 'pod_product_id'), 'classes': ('collapse',)}),
    )


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ['product', 'size', 'color', 'sku', 'stock']
    list_filter = ['size', 'color']
    search_fields = ['product__name', 'sku']
