from django.contrib import admin
from cloudmeb.prices.models import Price

class PriceAdmin(admin.ModelAdmin):
	fields = ('price_name', 'price_frequency', 'price_currency', 'price_formula', 'price_inputs',)
	list_display = ('price_name', 'price_frequency', 'price_currency', 'price_formula', 'admin_price_inputs',)
	filter_horizontal = ('price_inputs',)
	list_filter = ('price_frequency', 'price_currency',)

admin.site.register(Price, PriceAdmin)