from django.db import models
from cloudmeb.users.models import User
from cloudmeb.pages.models import Page
from cloudmeb.services.models import Service
from cloudmeb.products.models import Product
from django.utils.translation import ugettext_lazy as _
from cloudmeb.utils.i18n import bilingual_field
from django.utils.http import urlquote
from django.utils.translation import get_language

class Partner(User, Page):
	partner_id = models.AutoField(primary_key=True)
	partner_services = models.ManyToManyField(Service, verbose_name=_('services'), blank=True)
	partner_products = models.ManyToManyField(Product, verbose_name=_('products'), blank=True)
	partner_description_en = models.TextField(verbose_name=_('English description'))
	partner_description_fr = models.TextField(verbose_name=_('French description'))
	partner_description = bilingual_field('partner_description')
	partner_medium_description_en = models.TextField(verbose_name=_('English medium description'))
	partner_medium_description_fr = models.TextField(verbose_name=_('French medium description'))
	partner_medium_description = bilingual_field('partner_medium_description')
	partner_short_description_en = models.TextField(verbose_name=_('English short description'))
	partner_short_description_fr = models.TextField(verbose_name=_('French short description'))
	partner_short_description = bilingual_field('partner_short_description')

	class Meta:
		verbose_name = _('partner')
		verbose_name_plural = _('partners')

	def __str__(self):
		return self.get_full_name()

	def get_absolute_url(self):
		return '/%s/%s/%s' % (get_language(), _('partners'), urlquote(self.slug))

	def admin_partner_services(self):
		return '<ul>%s</ul>' % ''.join(['<li>%s</li>' % service for service in self.partner_services.all()])

	admin_partner_services.short_description = _('services')
	admin_partner_services.allow_tags = True

	def admin_partner_products(self):
		return '<ul>%s</ul>' % ''.join(['<li>%s</li>' % product for product in self.partner_products.all()])

	admin_partner_products.short_description = _('products')
	admin_partner_products.allow_tags = True
