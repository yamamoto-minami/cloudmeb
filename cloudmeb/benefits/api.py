from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from cloudmeb.benefits.models import Benefit

class BenefitResource(ModelResource):

	class Meta:
		queryset = Benefit.objects.all().distinct()
		resource_name = 'benefit'
		allowed_methods = ['get']
		filtering = {
			'name': ALL,
		}
