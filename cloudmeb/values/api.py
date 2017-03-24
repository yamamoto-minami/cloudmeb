from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from cloudmeb.values.models import Value
from cloudmeb.inputs.api import InputResource

class ValueResource(ModelResource):
	value_related_value = fields.ForeignKey('cloudmeb.values.api.ValueResource', 'value_related_value', full=True, null=True)
	value_input = fields.ForeignKey(InputResource, 'value_input', full=True, null=True)

	class Meta:
		queryset = Value.objects.all().distinct()
		resource_name = 'value'
		allowed_methods = ['get']
		filtering = {
			'name': ALL,
			'value_related_value': ALL_WITH_RELATIONS,
			'value_input': ALL_WITH_RELATIONS,
		}
