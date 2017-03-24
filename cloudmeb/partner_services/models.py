from django.db import models
from cloudmeb.partners.models import Partner
from cloudmeb.services.models import Service
from cloudmeb.prices.models import Price
from django.utils.translation import ugettext_lazy as _

class PartnerService(Price):
	partner_service_id = models.AutoField(primary_key=True)
	partner_service_service = models.ForeignKey(Service, blank=False, null=False, verbose_name=_('service'), related_name='partner_services')
	partner_service_partner = models.ForeignKey(Partner, blank=False, null=False, verbose_name=_('partner'))
	partner_service_featured = models.BooleanField(verbose_name=_('featured'))

	class Meta:
		verbose_name = _('partner service')
		verbose_name_plural = _('partner services')

	def __str__(self):
		return '%s %s' % (self.partner_service_partner, self.partner_service_service)

