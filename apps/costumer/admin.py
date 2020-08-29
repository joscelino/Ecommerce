from django.contrib import admin

from .models import Costumer, CostumerAddress


class CostumerAddressInline(admin.TabularInline):
    model = CostumerAddress
    extra = 0


class CostumerAdmin(admin.ModelAdmin):
    """ Master-Detail Costumer Panel """
    inlines = (CostumerAddressInline, )


admin.site.register(Costumer, CostumerAdmin)
