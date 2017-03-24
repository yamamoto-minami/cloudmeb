from django.db import models
from cloudmeb.utils.i18n import bilingual_field, bilingual_name, bilingual_field_name
from django.utils.translation import ugettext_lazy as _

PAGES = (
    ('WHY_CLOUDMEB', _('Why Cloudmeb')),
    ('PLUG_IN_YOUR_BUSINESS', _('Plug-in your business')),
    ('SOLUTIONS', _('Solutions')),
    ('BECOME_A_PARTNER', _('Become a partner')),
    ('CONTACT_US', _('Contact us')),
    ('FREQUENTLY_ASKED_QUESTIONS', _('Frequently asked questions')),
)

class Why_cloudmeb_txt(models.Model):
    why_cloudmeb_txt_id = models.AutoField(primary_key=True)
    why_cloudmeb_txt_name = models.CharField(verbose_name=_('page name'), max_length=100, choices=PAGES)
    why_cloudmeb_txt_header_title_en = models.CharField(verbose_name=_('english banner header title'), max_length=300, unique=True)
    why_cloudmeb_txt_header_title_fr = models.CharField(verbose_name=_('french banner header title'), max_length=300, unique=True)
    why_cloudmeb_txt_header_subtitle_en = models.CharField(verbose_name=_('english banner header sub title'), max_length=300, unique=True)
    why_cloudmeb_txt_header_subtitle_fr = models.CharField(verbose_name=_('french banner header sub title'), max_length=300, unique=True)
    why_cloudmeb_txt_introduce_title_en = models.CharField(verbose_name=_('english introduce title'), max_length=300, unique=True)
    why_cloudmeb_txt_introduce_title_fr = models.CharField(verbose_name=_('french introduce title'), max_length=300, unique=True)
    why_cloudmeb_txt_introduce_text_en = models.TextField(verbose_name=_('english introduce text'))
    why_cloudmeb_txt_introduce_text_fr = models.TextField(verbose_name=_('french introduce text'))
    why_cloudmeb_txt_why_introduce_title_en = models.CharField(verbose_name=_('english why introduce title'), max_length=300, unique=True)
    why_cloudmeb_txt_why_introduce_title_fr = models.CharField(verbose_name=_('french why introduce title'), max_length=300, unique=True)
    why_cloudmeb_txt_why_introduce_text_en = models.TextField(verbose_name=_('english why introduce text'))
    why_cloudmeb_txt_why_introduce_text_fr = models.TextField(verbose_name=_('french why introduce text'))
    why_cloudmeb_txt_whytab_title_en = models.CharField(verbose_name=_('english whytab title'), max_length=300, unique=True)
    why_cloudmeb_txt_whytab_title_fr = models.CharField(verbose_name=_('french whytab title'), max_length=300, unique=True)
    why_cloudmeb_txt_whytab_subtitle_en = models.CharField(verbose_name=_('english whytab sub title'), max_length=300, unique=True)
    why_cloudmeb_txt_whytab_subtitle_fr = models.CharField(verbose_name=_('french whytab sub title'), max_length=300, unique=True)
    why_cloudmeb_txt_cta_text_en = models.TextField(verbose_name=_('english cta text'))
    why_cloudmeb_txt_cta_text_fr = models.TextField(verbose_name=_('french cta text'))
    why_cloudmeb_txt_logo_slider_title_en = models.CharField(verbose_name=_('english logo slider title'), max_length=300, unique=True)
    why_cloudmeb_txt_logo_slider_title_fr = models.CharField(verbose_name=_('french logo slider title'), max_length=300, unique=True)
    why_cloudmeb_txt_experience_title_en = models.CharField(verbose_name=_('english experience title'), max_length=300, unique=True)
    why_cloudmeb_txt_experience_title_fr = models.CharField(verbose_name=_('french experience title'), max_length=300, unique=True)
    why_cloudmeb_txt_testimonial_title_en = models.CharField(verbose_name=_('english testimonial title'), max_length=300, unique=True)
    why_cloudmeb_txt_testimonial_title_fr = models.CharField(verbose_name=_('french testimonial title'), max_length=300, unique=True)

    class Meta:
        verbose_name = _('why_cloudmeb_txt')
        verbose_name_plural = _('why_cloudmeb_txts')

    def __str__(self):
        return self.why_cloudmeb_txt_name

    def is_default(self, this, field):
        return self._meta.get_field(field).get_default() == str(getattr(this, field))

    def save(self, *args, **kwargs):
        super(Why_cloudmeb_txt, self).save(*args, **kwargs)
