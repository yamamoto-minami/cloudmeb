from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from cloudmeb.inputs.models import Input

class InputResource(ModelResource):
	input_default_value = fields.ForeignKey('cloudmeb.values.api.ValueResource', 'input_default_value', full=True, null=True)

	class Meta:
		queryset = Input.objects.all().distinct()
		resource_name = 'input'
		allowed_methods = ['get']
		filtering = {
			'name': ALL,
			'input_default_value': ALL_WITH_RELATIONS,
		}