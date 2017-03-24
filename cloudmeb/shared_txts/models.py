from django.db import models
from cloudmeb.utils.i18n import bilingual_field
from django.utils.translation import ugettext_lazy as _

class Shared_txt(models.Model):
   
    shared_txt_id = models.AutoField(primary_key=True)
    shared_txt_name = models.CharField(verbose_name=_('shared name'), max_length=300, unique=True)
    shared_txt_name_en = models.CharField(verbose_name=_('shared name english'), max_length=300, unique=True)
    shared_txt_name_fr = models.CharField(verbose_name=_('shared name french'), max_length=300, unique=True)

    class Meta:
        verbose_name = _('shared_txt')
        verbose_name_plural = _('shared_txts')

    def __str__(self):
        return self.shared_txt_name

    def is_default(self, this, field):
        return self._meta.get_field(field).get_default() == str(getattr(this, field))

    def save(self, *args, **kwargs):
        super(Shared_txt, self).save(*args, **kwargs)
