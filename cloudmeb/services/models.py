from django.db import models
from cloudmeb.pages.models import Page
from cloudmeb.solutions.models import Solution
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language

class Service(Solution, Page):
    service_id = models.AutoField(primary_key=True)
    service_order = models.IntegerField(verbose_name=_('order'), unique=True, blank=False)
    service_debug = models.TextField(verbose_name=_('debug'), default='debug')

    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')

    def __str__(self):
        return self.solution_name

    def get_absolute_url(self):
        return '/%s/%s/%s' % (get_language(), _('services'), self.solution_slug)
