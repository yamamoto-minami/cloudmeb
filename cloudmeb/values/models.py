from django.db import models
from cloudmeb.utils.i18n import bilingual_field
from django.utils.translation import ugettext_lazy as _

VALUE_TYPES = (
	('STRING', _('String')),
	('INTEGER', _('Integer')),
	('BOOLEAN', _('Boolean')),
	('WILDCARD', _('Wildcard')),
)

class Value(models.Model):
	value_id = models.AutoField(primary_key=True)
	value_type = models.CharField(verbose_name=_('type'), max_length=100, choices=VALUE_TYPES)
	value_name_en = models.CharField(verbose_name=_('english name'), max_length=200, unique=False)
	value_name_fr = models.CharField(verbose_name=_('french name'), max_length=200, unique=False)
	value_name = bilingual_field('value_name')
	value_value = models.CharField(verbose_name=_('value'), blank=True, null=True, max_length=200, unique=False)
	value_order = models.IntegerField(verbose_name=_('order'), unique=False, blank=True, null=True)
	value_input = models.ForeignKey('inputs.Input', blank=True, null=True, verbose_name='input', related_name='values')
	value_related_value = models.ForeignKey('self', blank=True, null=True, verbose_name=_('related value'))

	class Meta:
		verbose_name = _('value')
		verbose_name_plural = _('values')
		ordering = ['value_order']

	def __str__(self):
		return '%s : %s' % (self.value_name, self.value_input)
