from django.db import models
from cloudmeb.seos.models import Seo
from django.utils.translation import ugettext_lazy as _

PAGES = (
    ('WHY_CLOUDMEB', _('Why Cloudmeb')),
    ('PLUG_IN_YOUR_BUSINESS', _('Plug-in your business')),
    ('PRICING', _('Pricing')),
    ('SOLUTIONS', _('Solutions')),
    ('BECOME_A_PARTNER', _('Become a partner')),
    ('CONTACT_US', _('Contact us')),
    ('FREQUENTLY_ASKED_QUESTIONS', _('Frequently asked questions')),
    ('TERMS_OF_USE', _('Terms of use')),
    ('BOOK_NOW', _('Book now')),
    ('PRIVACY_POLICY', _('Privacy policy')),
    ('DYNAMIC_PARTNER', _('Dynamic partner')),
    ('DYNAMIC_SERVICE', _('Dynamic service')),
    ('DYNAMIC_PRODUCT', _('Dynamic product')),
)

class Page(Seo):
    page_id = models.AutoField(primary_key=True)
    page_name = models.CharField(verbose_name=_('page name'), max_length=100, choices=PAGES, default='page name')
    

    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')

    def __str__(self):
        return self.page_name
