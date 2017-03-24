from django.contrib import admin
from cloudmeb.partner_services.models import PartnerService
from cloudmeb.prices.admin import PriceAdmin
from django.utils.translation import ugettext_lazy as _

class PartnerServiceAdmin(admin.ModelAdmin):
	fieldsets = (
		(_('Partner and service'), {
			'fields': ('partner_service_partner', 'partner_service_service', 'partner_service_featured',)
		}),
		(_('Pricing'), {
			'fields': PriceAdmin.fields
		}),
	)
	list_display = ('partner_service_partner', 'partner_service_service', 'partner_service_featured',) + PriceAdmin.list_display
	filter_horizontal = PriceAdmin.filter_horizontal
	list_filter = ('partner_service_featured',) + PriceAdmin.list_filter

admin.site.register(PartnerService, PartnerServiceAdmin)