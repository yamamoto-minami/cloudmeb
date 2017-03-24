from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from cloudmeb.partners.models import Partner
from cloudmeb.users.admin import UserAdmin
from cloudmeb.pages.admin import PageAdmin
from django.utils.translation import ugettext_lazy as _

class PartnerAdmin(BaseUserAdmin):
	descriptions = ('partner_description_en', 'partner_description_fr', 'partner_medium_description_en', 'partner_medium_description_fr', 'partner_short_description_en', 'partner_short_description_fr',)
	fieldsets = (
		(_('Basic info'), {
			'fields': UserAdmin.basic_info
		}),
		(_('Personal info'), {
			'fields': UserAdmin.personal_info + descriptions
		}),
		(_('Permissions'), {
			'classes': ('collapse',),
			'fields': UserAdmin.permissions
		}),
		(_('Important dates'), {
			'fields': UserAdmin.important_dates
		}),
		(_('Products and Services'), {
			'fields': ('partner_services', 'partner_products',)
		}),
		(_('Page info'), {
			'fields': PageAdmin.fields + ('slug',)
		}),
	)
	add_fieldsets = UserAdmin.add_fieldsets
	list_display = UserAdmin.list_display + ('admin_partner_services', 'admin_partner_products',) + descriptions + PageAdmin.list_display
	search_fields = UserAdmin.search_fields
	readonly_fields = ('admin_partner_services', 'admin_partner_products',) + UserAdmin.readonly_fields + PageAdmin.readonly_fields
	ordering = UserAdmin.ordering
	filter_horizontal = ('partner_services', 'partner_products',) + UserAdmin.filter_horizontal
	inlines = UserAdmin.inlines
	list_filter = UserAdmin.list_filter

admin.site.register(Partner, PartnerAdmin)
