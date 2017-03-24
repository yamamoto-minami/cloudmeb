from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from cloudmeb.partner_services.models import PartnerService

class PartnerServiceResource(ModelResource):
	partner_service_service = fields.ForeignKey('cloudmeb.services.api.ServiceResource', 'partner_service_service', full=True, null=True)
	partner_service_partner = fields.ForeignKey('cloudmeb.partners.api.PartnerResource', 'partner_service_partner', full=True, null=True)
	price_inputs = fields.ToManyField('cloudmeb.inputs.api.InputResource', 'price_inputs', full=True, null=True)

	class Meta:
		queryset = PartnerService.objects.all().distinct()
		resource_name = 'partner_service'
		allowed_methods = ['get']
		filtering = {
			'name': ALL,
			'partner_service_service': ALL_WITH_RELATIONS,
			'partner_service_partner': ALL_WITH_RELATIONS,
			'price_inputs': ALL_WITH_RELATIONS,
		}