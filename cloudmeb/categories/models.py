from django.db import models
from cloudmeb.utils.i18n import bilingual_field
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
	category_id = models.AutoField(primary_key=True)
	category_name_en = models.CharField(verbose_name=_('english name'), max_length=200, unique=True)
	category_name_fr = models.CharField(verbose_name=_('french name'), max_length=200, unique=True)
	category_name = bilingual_field('category_name')
	category_short_name_en = models.CharField(verbose_name=_('english short name'), max_length=100, unique=True)
	category_short_name_fr = models.CharField(verbose_name=_('french short name'), max_length=100, unique=True)
	category_short_name = bilingual_field('category_short_name')

	class Meta:
		verbose_name = _('category')
		verbose_name_plural = _('categories')

	def __str__(self):
		return self.category_name
