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

class Become_partner_txt(models.Model):

    become_partner_txt_id = models.AutoField(primary_key=True)
    become_partner_txt_name = models.CharField(verbose_name=_('page name'), max_length=100, choices=PAGES)
    become_partner_txt_header_title_en = models.CharField(verbose_name=_('english banner header title'), max_length=300, unique=True)
    become_partner_txt_header_title_fr = models.CharField(verbose_name=_('french banner header title'), max_length=300, unique=True)
    become_partner_txt_header_subtitle_en = models.CharField(verbose_name=_('english banner header sub title'), max_length=300, unique=True)
    become_partner_txt_header_subtitle_fr = models.CharField(verbose_name=_('french banner header sub title'), max_length=300, unique=True)
    become_partner_txt_content_title_en = models.CharField(verbose_name=_('english content title'), max_length=300, unique=True)
    become_partner_txt_content_title_fr = models.CharField(verbose_name=_('french content title'), max_length=300, unique=True)
    become_partner_txt_content_level1_title_en = models.CharField(verbose_name=_('english content level1 title'), max_length=300, unique=True)
    become_partner_txt_content_level1_title_fr = models.CharField(verbose_name=_('french content level1 title'), max_length=300, unique=True)
    become_partner_txt_content_level1_text_en = models.TextField(verbose_name=_('english content level1 text'))
    become_partner_txt_content_level1_text_fr = models.TextField(verbose_name=_('french content level1 text'))
    become_partner_txt_content_level11_title_en = models.CharField(verbose_name=_('english content level11 title'), max_length=300, unique=True)
    become_partner_txt_content_level11_title_fr = models.CharField(verbose_name=_('french content level11 title'), max_length=300, unique=True)
    become_partner_txt_content_level11_text_en = models.TextField(verbose_name=_('english content level11 text'))
    become_partner_txt_content_level11_text_fr = models.TextField(verbose_name=_('french content level11 text'))
    become_partner_txt_content_level12_title_en = models.CharField(verbose_name=_('english content level12 title'), max_length=300, unique=True)
    become_partner_txt_content_level12_title_fr = models.CharField(verbose_name=_('french content level12 title'), max_length=300, unique=True)
    become_partner_txt_content_level12_text_en = models.TextField(verbose_name=_('english content level12 text'))
    become_partner_txt_content_level12_text_fr = models.TextField(verbose_name=_('french content level12 text'))
    become_partner_txt_content_level13_title_en = models.CharField(verbose_name=_('english content level13 title'), max_length=300, unique=True)
    become_partner_txt_content_level13_title_fr = models.CharField(verbose_name=_('french content level13 title'), max_length=300, unique=True)
    become_partner_txt_content_level13_text_en = models.TextField(verbose_name=_('english content level13 text'))
    become_partner_txt_content_level13_text_fr = models.TextField(verbose_name=_('french content level13 text'))
    become_partner_txt_content_level2_title_en = models.CharField(verbose_name=_('english content level2 title'), max_length=300, unique=True)
    become_partner_txt_content_level2_title_fr = models.CharField(verbose_name=_('french content level2 title'), max_length=300, unique=True)
    become_partner_txt_content_level2_text_en = models.TextField(verbose_name=_('english content level2 text'))
    become_partner_txt_content_level2_text_fr = models.TextField(verbose_name=_('french content level2 text'))
    become_partner_txt_content_level21_title_en = models.CharField(verbose_name=_('english content level21 title'), max_length=300, unique=True)
    become_partner_txt_content_level21_title_fr = models.CharField(verbose_name=_('french content level21 title'), max_length=300, unique=True)
    become_partner_txt_content_level21_text_en = models.TextField(verbose_name=_('english content level21 text'))
    become_partner_txt_content_level21_text_fr = models.TextField(verbose_name=_('french content level21 text'))
    become_partner_txt_content_level22_title_en = models.CharField(verbose_name=_('english content level22 title'), max_length=300, unique=True)
    become_partner_txt_content_level22_title_fr = models.CharField(verbose_name=_('french content level22 title'), max_length=300, unique=True)
    become_partner_txt_content_level22_text_en = models.TextField(verbose_name=_('english content level22 text'))
    become_partner_txt_content_level22_text_fr = models.TextField(verbose_name=_('french content level22 text'))
    become_partner_txt_content_level23_title_en = models.CharField(verbose_name=_('english content level23 title'), max_length=300, unique=True)
    become_partner_txt_content_level23_title_fr = models.CharField(verbose_name=_('french content level23 title'), max_length=300, unique=True)
    become_partner_txt_content_level23_text_en = models.TextField(verbose_name=_('english content level23 text'))
    become_partner_txt_content_level23_text_fr = models.TextField(verbose_name=_('french content level23 text'))
    become_partner_txt_content_level3_title_en = models.CharField(verbose_name=_('english content level3 title'), max_length=300, unique=True)
    become_partner_txt_content_level3_title_fr = models.CharField(verbose_name=_('french content level3 title'), max_length=300, unique=True)
    become_partner_txt_content_level3_text_en = models.TextField(verbose_name=_('english content level3 text'))
    become_partner_txt_content_level3_text_fr = models.TextField(verbose_name=_('french content level3 text'))
    become_partner_txt_content_level31_title_en = models.CharField(verbose_name=_('english content level31 title'), max_length=300, unique=True)
    become_partner_txt_content_level31_title_fr = models.CharField(verbose_name=_('french content level31 title'), max_length=300, unique=True)
    become_partner_txt_content_level31_text_en = models.TextField(verbose_name=_('english content level31 text'))
    become_partner_txt_content_level31_text_fr = models.TextField(verbose_name=_('french content level31 text'))
    become_partner_txt_content_level32_title_en = models.CharField(verbose_name=_('english content level32 title'), max_length=300, unique=True)
    become_partner_txt_content_level32_title_fr = models.CharField(verbose_name=_('french content level32 title'), max_length=300, unique=True)
    become_partner_txt_content_level32_text_en = models.TextField(verbose_name=_('english content level32 text'))
    become_partner_txt_content_level32_text_fr = models.TextField(verbose_name=_('french content level32 text'))
    become_partner_txt_content_level33_title_en = models.CharField(verbose_name=_('english content level33 title'), max_length=300, unique=True)
    become_partner_txt_content_level33_title_fr = models.CharField(verbose_name=_('french content level33 title'), max_length=300, unique=True)
    become_partner_txt_content_level33_text_en = models.TextField(verbose_name=_('english content level33 text'))
    become_partner_txt_content_level33_text_fr = models.TextField(verbose_name=_('french content level33 text'))
    become_partner_txt_step_title_en = models.CharField(verbose_name=_('english step title'), max_length=300, unique=True)
    become_partner_txt_step_title_fr = models.CharField(verbose_name=_('french step title'), max_length=300, unique=True)
    become_partner_txt_step_subtitle1_en = models.CharField(verbose_name=_('english step subtitle1'), max_length=300, unique=True)
    become_partner_txt_step_subtitle1_fr = models.CharField(verbose_name=_('french step subtitle1'), max_length=300, unique=True)
    become_partner_txt_step_subtext1_en = models.TextField(verbose_name=_('english step subtext1 text'))
    become_partner_txt_step_subtext1_fr = models.TextField(verbose_name=_('french step subtext1 text'))
    become_partner_txt_step_subtitle2_en = models.CharField(verbose_name=_('english step subtitle2'), max_length=300, unique=True)
    become_partner_txt_step_subtitle2_fr = models.CharField(verbose_name=_('french step subtitle2'), max_length=300, unique=True)
    become_partner_txt_step_subtext2_en = models.TextField(verbose_name=_('english step subtext2 text'))
    become_partner_txt_step_subtext2_fr = models.TextField(verbose_name=_('french step subtext2 text'))
    become_partner_txt_step_subtitle3_en = models.CharField(verbose_name=_('english step subtitle3'), max_length=300, unique=True)
    become_partner_txt_step_subtitle3_fr = models.CharField(verbose_name=_('french step subtitle3'), max_length=300, unique=True)
    become_partner_txt_step_subtext3_en = models.TextField(verbose_name=_('english step subtext3 text'))
    become_partner_txt_step_subtext3_fr = models.TextField(verbose_name=_('french step subtext3 text'))
    become_partner_txt_say_title_en = models.CharField(verbose_name=_('english partner say title'), max_length=300, unique=True)
    become_partner_txt_say_title_fr = models.CharField(verbose_name=_('french partner say title'), max_length=300, unique=True)
    become_partner_txt_form_title_en = models.CharField(verbose_name=_('english step form title'), max_length=300, unique=True)
    become_partner_txt_form_title_fr = models.CharField(verbose_name=_('french step form title'), max_length=300, unique=True)
    become_partner_txt_form_text_en = models.TextField(verbose_name=_('english step form text'))
    become_partner_txt_form_text_fr = models.TextField(verbose_name=_('french step form text'))
    become_partner_txt_form_test = models.TextField(verbose_name=_('test'), default='test')

    class Meta:
        verbose_name = _('become_partner_txt')
        verbose_name_plural = _('become_partner_txts')

    def __str__(self):
        return self.become_partner_txt_name

    def is_default(self, this, field):
        return self._meta.get_field(field).get_default() == str(getattr(this, field))

    def save(self, *args, **kwargs):
        super(Become_partner_txt, self).save(*args, **kwargs)




