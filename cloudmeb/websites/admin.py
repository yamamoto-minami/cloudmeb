from django.contrib import admin
from django.contrib.sites.models import Site
from cloudmeb.websites.models import Website
from cloudmeb.websites.forms import WebsiteForm
from django.utils.translation import ugettext_lazy as _

class WebsiteAdmin(admin.ModelAdmin):
	form = WebsiteForm
	fieldsets = (
		(_('Domain info'), {
			'fields': ('name', 'domain',)
		}),
		(_('Smtp info'), {
			'fields': ('smtp_user', 'smtp_password', 'smtp_from_email', 'smtp_server', 'smtp_port', 'smtp_tls',)
		}),
		(_('Connection info'), {
			'fields': ('salesforce_id', 'hotjar_id', 'add_this_id', 'facebook_pixel_id', 'facebook_admin_id', 'bing_analytics_id', 'google_analytics_id', 'google_addwords_id', 'personal_google_plus_url', 'google_plus_url', 'twitter_url', 'facebook_url', 'linkedin_url', 'shop_url',)
		}),
	)
	list_display = ('name', 'domain', 'smtp_user', 'smtp_from_email', 'smtp_server', 'smtp_port', 'smtp_tls', 'salesforce_id', 'add_this_id', 'facebook_admin_id', 'bing_analytics_id', 'google_analytics_id', 'google_addwords_id', 'personal_google_plus_url', 'google_plus_url', 'twitter_url', 'facebook_url', 'linkedin_url', 'shop_url',)

admin.site.unregister(Site)
admin.site.register(Website, WebsiteAdmin)
