from django.contrib import admin
from cloudmeb.products.models import Product
from cloudmeb.solutions.admin import SolutionAdmin
from cloudmeb.prices.admin import PriceAdmin
from cloudmeb.pages.admin import PageAdmin
from django.utils.translation import ugettext_lazy as _

class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Basic'), {
            'fields': SolutionAdmin.info + ('product_url', 'product_order', 'product_featured',)
        }),
        (_('Page'), {
            'fields': PageAdmin.fields
        }),
        (_('Media'), {
            'fields': SolutionAdmin.medias
        }),
        (_('Benefits'), {
            'fields': SolutionAdmin.benefits
        }),
        (_('Values'), {
            'fields': SolutionAdmin.values
        }),
        (_('Categories'), {
            'fields': SolutionAdmin.categories
        }),
        (_('Pricing info'), {
            'fields': PriceAdmin.fields
        }),
    )
    list_display = SolutionAdmin.list_display + PriceAdmin.list_display + PageAdmin.list_display + ('product_url', 'product_order', 'product_featured',)
    readonly_fields = SolutionAdmin.readonly_fields + PageAdmin.readonly_fields
    filter_horizontal = SolutionAdmin.filter_horizontal + PriceAdmin.filter_horizontal
    list_filter = ('product_featured',) + PageAdmin.list_filter + PriceAdmin.list_filter
    search_fields = SolutionAdmin.search_fields

admin.site.register(Product, ProductAdmin)
