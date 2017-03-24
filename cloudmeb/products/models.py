from django.db import models
from cloudmeb.pages.models import Page
from cloudmeb.prices.models import Price
from cloudmeb.solutions.models import Solution
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from cloudmeb.utils.i18n import bilingual_field
from django.utils.translation import get_language

class Product(Solution, Price, Page):
	product_id = models.AutoField(primary_key=True)
	product_url = models.URLField(verbose_name='site url', blank=True)
	product_featured = models.BooleanField(verbose_name=_('featured'))
	product_order = models.IntegerField(verbose_name=_('order'), unique=True, blank=False)

	class Meta:
		verbose_name = _('product')
		verbose_name_plural = _('products')

	def __str__(self):
		return self.solution_name

	def get_absolute_url(self):
		return '/%s/%s/%s' % (get_language(), _('products'), self.solution_slug)