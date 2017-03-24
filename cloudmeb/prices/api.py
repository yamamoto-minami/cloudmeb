from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from cloudmeb.prices.models import Price

class PriceResource(ModelResource):
	price_inputs = fields.ToManyField('cloudmeb.inputs.api.InputResource', 'price_inputs', full=True, null=True)

	class Meta:
		queryset = Price.objects.all().distinct()
		resource_name = 'price'
		allowed_methods = ['get']
		filtering = {
			'name': ALL,
			'price_inputs': ALL_WITH_RELATIONS,
		}