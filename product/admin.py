from django.contrib import admin

from .models import Product, Variation


class VariationInline(admin.TabularInline):
    model = Variation
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    """ Master-Detail Product Panel """
    inlines = (VariationInline, )
    list_display = ('name', 'short_description', 'get_formatted_price',
                    'get_formatted_promotional_price', 'product_type', 'slug')
    list_display_links = ('name',)
    list_filter = ('name', )


admin.site.register(Product, ProductAdmin)
