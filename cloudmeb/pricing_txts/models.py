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

class Pricing_txt(models.Model):
   
    Pricing_txt_id = models.AutoField(primary_key=True)
    Pricing_txt_name = models.CharField(verbose_name=_('page name'), max_length=100, choices=PAGES)
    Pricing_txt_header_title_en = models.CharField(verbose_name=_('english banner header title'), max_length=300, unique=True)
    Pricing_txt_header_title_fr = models.CharField(verbose_name=_('french banner header title'), max_length=300, unique=True)
    Pricing_txt_header_subtitle_en = models.CharField(verbose_name=_('english banner header sub title'), max_length=300, unique=True)
    Pricing_txt_header_subtitle_fr = models.CharField(verbose_name=_('french banner header sub title'), max_length=300, unique=True)
    Pricing_txt_product_title_en = models.CharField(verbose_name=_('english product title'), max_length=300, unique=True)
    Pricing_txt_product_title_fr = models.CharField(verbose_name=_('french product title'), max_length=300, unique=True)
    Pricing_txt_service_title_en = models.CharField(verbose_name=_('english service title'), max_length=300, unique=True)
    Pricing_txt_service_title_fr = models.CharField(verbose_name=_('french service title'), max_length=300, unique=True)
    Pricing_txt_showbtn_product_en = models.TextField(verbose_name=_('english Show more product button text'))
    Pricing_txt_showbtn_product_fr = models.TextField(verbose_name=_('french Show more product button text'))    
    Pricing_txt_showbtn_service_en = models.TextField(verbose_name=_('english Show more service button text'))
    Pricing_txt_showbtn_service_fr = models.TextField(verbose_name=_('french Show more service button text'))    
    Pricing_txt_monthly_title_en = models.TextField(verbose_name=_('english monthly title'))
    Pricing_txt_monthly_title_fr = models.TextField(verbose_name=_('french monthly title'))
    Pricing_txt_monthly_subtitle_en = models.TextField(verbose_name=_('english monthly subtitle'))
    Pricing_txt_monthly_subtitle_fr = models.TextField(verbose_name=_('french monthly subtitle'))
    Pricing_txt_monthly_btn_en = models.CharField(verbose_name=_('english monthly button'), max_length=300, unique=True)
    Pricing_txt_monthly_btn_fr = models.CharField(verbose_name=_('french monthly button'), max_length=300, unique=True)
    Pricing_txt_onetime_title_en = models.TextField(verbose_name=_('english onetime title'))
    Pricing_txt_onetime_title_fr = models.TextField(verbose_name=_('french onetime title'))
    Pricing_txt_onetime_subtitle_en = models.TextField(verbose_name=_('english onetime subtitle'))
    Pricing_txt_onetime_subtitle_fr = models.TextField(verbose_name=_('french onetime subtitle'))
    Pricing_txt_onetime_btn_en = models.CharField(verbose_name=_('english onetime button'), max_length=300, unique=True)
    Pricing_txt_onetime_btn_fr = models.CharField(verbose_name=_('french onetime button'), max_length=300, unique=True)
    

    class Meta:
		    verbose_name = _('pricing_txt')
		    verbose_name_plural = _('pricing_txts')

    def __str__(self):
    		return self.Pricing_txt_name

    def is_default(self, this, field):
        return self._meta.get_field(field).get_default() == str(getattr(this, field))

    def save(self, *args, **kwargs):
    		super(Pricing_txt, self).save(*args, **kwargs)
