from django.contrib import admin
from cloudmeb.inputs.models import Input
from cloudmeb.values.models import Value

class ValueInline(admin.StackedInline):
	model = Value
	extra = 1

class InputAdmin(admin.ModelAdmin):
	list_display = ('input_label_en', 'input_label_fr', 'input_question_en', 'input_question_fr', 'input_placeholder_en', 'input_placeholder_fr', 'input_name', 'input_type', 'input_default_value', 'input_related_input', 'admin_input_values', 'input_display', 'input_salesforce_id', 'input_order',)
	inlines = [ValueInline,]
	list_filter = ('input_type', 'input_display',)
	search_fields = ['input_label_en', 'input_label_fr', 'input_question_en', 'input_question_fr', 'input_placeholder_en', 'input_placeholder_fr', 'input_name', 'input_salesforce_id',]

admin.site.register(Input, InputAdmin)