from django.contrib import admin

from .models import Product, Variation


class VariationInline(admin.TabularInline):
    model = Variation
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    """ Master-Detail Product Panel """
    inlines = (VariationInline, )


admin.site.register(Product, ProductAdmin)
