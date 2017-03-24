from django.db import models
from cloudmeb.values.models import Value
from cloudmeb.utils.i18n import bilingual_field
from django.utils.translation import ugettext_lazy as _

INPUT_TYPES = (
	('OPTIONS', _('Options')),
	('MULTI_OPTIONS', _('Multi options')),
	('RADIO', _('Radio')),
	('CHECKBOX', _('Checkbox')),
	('NUMBER', _('Number')),
)

class Input(models.Model):
	input_id = models.AutoField(primary_key=True)
	input_type = models.CharField(verbose_name=_('type'), max_length=100, choices=INPUT_TYPES)
	input_name = models.CharField(verbose_name=_('name'), max_length=50, unique=False)
	input_salesforce_id = models.CharField(verbose_name=_('salesforce id'), blank=True, null=True, max_length=50, unique=False)
	input_label_en = models.CharField(verbose_name=_('english label'), max_length=200, unique=False)
	input_label_fr = models.CharField(verbose_name=_('french label'),max_length=200, unique=False)
	input_label = bilingual_field('input_label')
	input_question_en = models.CharField(verbose_name=_('english question'), max_length=500, unique=False, blank=True)
	input_question_fr = models.CharField(verbose_name=_('french question'),max_length=500, unique=False, blank=True)
	input_question = bilingual_field('input_question')
	input_placeholder_en = models.CharField(verbose_name=_('english placeholder'), max_length=200, unique=False, blank=True)
	input_placeholder_fr = models.CharField(verbose_name=_('french placeholder'), max_length=200, unique=False, blank=True)
	input_placeholder = bilingual_field('input_placeholder')
	input_default_value = models.ForeignKey('values.Value', verbose_name=_('default value'), blank=True, null=True)
	input_related_input = models.ForeignKey('self', blank=True, null=True, verbose_name=_('related input'))
	input_order = models.IntegerField(verbose_name=_('order'), unique=False, blank=True, null=True)
	input_display = models.BooleanField(verbose_name='display', default=False)

	class Meta:
		verbose_name = _('input')
		verbose_name_plural = _('inputs')

	def __str__(self):
		return '%s : %s%s%s' % (self.input_label, '%(', self.input_name, ')s')

	def admin_input_values(self):
		values = Value.objects.filter(value_input=self.input_id)
		return '<ul>%s</ul>' % ''.join(['<li>%s</li>' % value for value in values])

	admin_input_values.short_description = _('values')
	admin_input_values.allow_tags = True