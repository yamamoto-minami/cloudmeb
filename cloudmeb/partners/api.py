from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from cloudmeb.partners.models import Partner

class PartnerResource(ModelResource):
	partner_services = fields.ToManyField('cloudmeb.services.api.ServiceResource', 'partner_services', full=True, null=True)
	partner_products = fields.ToManyField('cloudmeb.products.api.ProductResource', 'partner_products', full=True, null=True)

	class Meta:
		queryset = Partner.objects.all().distinct()
		resource_name = 'partner'
		allowed_methods = ['get']
		excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined']

		filtering = {
			'name': ALL,
			'partner_services': ALL_WITH_RELATIONS,
			'partner_products': ALL_WITH_RELATIONS,
		}
