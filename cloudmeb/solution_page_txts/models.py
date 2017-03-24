from django.db import models
from cloudmeb.utils.i18n import bilingual_field
from django.utils.translation import ugettext_lazy as _

PAGES = (
     ('WHY_CLOUDMEB', _('Why Cloudmeb')),
     ('PLUG_IN_YOUR_BUSINESS', _('Plug-in your business')),
     ('SOLUTIONS', _('Solutions')),
     ('BECOME_A_PARTNER', _('Become a partner')),
     ('CONTACT_US', _('Contact us')),
     ('FREQUENTLY_ASKED_QUESTIONS', _('Frequently asked questions')),
)

class Solution_page_txt(models.Model):

    solution_page_txt_id = models.AutoField(primary_key=True)
    solution_page_txt_name = models.CharField(verbose_name=_('page name'), max_length=100, choices=PAGES)
    solution_page_txt_header_title_en = models.CharField(verbose_name=_('english banner header title'), max_length=300, unique=True)
    solution_page_txt_header_title_fr = models.CharField(verbose_name=_('french banner header title'), max_length=300, unique=True)
    solution_page_txt_header_subtitle_en = models.CharField(verbose_name=_('english banner header sub title'), max_length=300, unique=True)
    solution_page_txt_header_subtitle_fr = models.CharField(verbose_name=_('french banner header sub title'), max_length=300, unique=True)
    solution_page_txt_product_title_en = models.CharField(verbose_name=_('english product title'), max_length=300, unique=True)
    solution_page_txt_product_title_fr = models.CharField(verbose_name=_('french product title'), max_length=300, unique=True)
    solution_page_txt_service_title_en = models.CharField(verbose_name=_('english service title'), max_length=300, unique=True)
    solution_page_txt_service_title_fr = models.CharField(verbose_name=_('french service title'), max_length=300, unique=True)
    solution_page_txt_cta_text_en = models.TextField(verbose_name=_('english cta text'))
    solution_page_txt_cta_text_fr = models.TextField(verbose_name=_('french cta text'))  

    class Meta:
        verbose_name = _('solution_page_txt')
        verbose_name_plural = _('solution_page_txts')
    
    def __str__(self):
        return self.solution_page_txt_name

    def is_default(self, this, field):
        return self._meta.get_field(field).get_default() == str(getattr(this, field))

    def save(self, *args, **kwargs):
        super(Solution_page_txt, self).save(*args, **kwargs)
