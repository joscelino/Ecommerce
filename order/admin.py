from django.contrib import admin
from .models import Order, ItemOrder


class ItemOrderInline(admin.TabularInline):
    model = ItemOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    """ Master-Detail Order Panel """
    inlines = (ItemOrderInline, )


admin.site.register(Order, OrderAdmin)
