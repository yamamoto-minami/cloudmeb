from django.db import models
from cloudmeb.inputs.models import Input
from django.utils.translation import ugettext_lazy as _
from cloudmeb.utils.i18n import bilingual_field

FREQUENCIES = (
	('ONE_TIME', _('One time')),
	('MONTHLY', _('Monthly')),
	('QUARTERLY', _('Quarterly')),
	('SEMI_ANNUAL', _('Semi anual')),
	('ANNUAL', _('Annual')),
)

CURRENCIES = (
	('USD', _('US dollar')),
	('CAD', _('Canadian dollar')),
)

class Price(models.Model):
	price_id = models.AutoField(primary_key=True)
	price_name = models.CharField(verbose_name=_('name'), max_length=60, unique=True)
	price_frequency = models.CharField(verbose_name=_('billing frequency'), max_length=100, choices=FREQUENCIES)
	price_currency = models.CharField(verbose_name=_('billing currency'), max_length=100, choices=CURRENCIES)
	price_inputs = models.ManyToManyField(Input, verbose_name='inputs', blank=True)
	price_formula = models.TextField(verbose_name=_('formula'), blank=False, default='0')

	class Meta:
		verbose_name = _('price')
		verbose_name_plural = _('Prices')

	def __str__(self):
		return self.price_name

	def admin_price_inputs(self):
		return '<ul>%s</ul>' % ''.join(['<li>%s</li>' % price_input for price_input in self.price_inputs.all()])

	admin_price_inputs.short_description = _('inputs')
	admin_price_inputs.allow_tags = True
