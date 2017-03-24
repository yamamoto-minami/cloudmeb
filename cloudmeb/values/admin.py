from django.contrib import admin
from cloudmeb.values.models import Value

class ValueAdmin(admin.ModelAdmin):
	list_display = ('value_name_en', 'value_name_fr', 'value_type', 'value_value', 'value_order', 'value_input', 'value_related_value',)
	list_filter = ('value_type',)
	search_fields = ['value_name_en', 'value_name_fr', 'value_value',]

admin.site.register(Value, ValueAdmin)