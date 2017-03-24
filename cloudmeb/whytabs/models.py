from django.db import models
from cloudmeb.utils.i18n import bilingual_field, bilingual_name
from django.utils.translation import ugettext_lazy as _

class Whytab(models.Model):
    whytab_id = models.AutoField(primary_key=True)
    whytab_class_name = models.CharField(verbose_name=_('class name'), max_length=200, unique=True)
    whytab_menu_name_en = models.CharField(verbose_name=_('english menu name'), max_length=200, unique=True)
    whytab_menu_name_fr = models.CharField(verbose_name=_('french menu name'),max_length=200, unique=True)
    whytab_menu_name = bilingual_field('whytab_menu_name')
    whytab_left_title_en = models.CharField(verbose_name=_('english left title name'),max_length=200, unique=True)
    whytab_left_title_fr = models.CharField(verbose_name=_('french left title name'),max_length=200, unique=True)
    whytab_left_title = bilingual_field('whytab_left_title')
    whytab_left_content_en = models.TextField(verbose_name=_('english left content'), max_length=1000, unique=True)
    whytab_left_content_fr = models.TextField(verbose_name=_('french left content'), max_length=1000, unique=True)
    whytab_left_content = bilingual_field('whytab_left_content')
    whytab_left_icon = models.ImageField(verbose_name=_('leftside icon'), upload_to='whytabs/', default='placeholders/50x50.gif', blank=False)
    whytab_right_title_en = models.CharField(verbose_name=_('english right title name'),max_length=200, unique=True)
    whytab_right_title_fr = models.CharField(verbose_name=_('french right title name'),max_length=200, unique=True)
    whytab_right_title = bilingual_field('whytab_right_title')
    whytab_right_content_en = models.TextField(verbose_name=_('english right content'), max_length=1000, unique=True)
    whytab_right_content_fr = models.TextField(verbose_name=_('french right content'), max_length=1000, unique=True)
    whytab_right_content = bilingual_field('whytab_right_content')
    whytab_right_slug_en = models.CharField(verbose_name=_('english right slug name'),max_length=200, unique=True)
    whytab_right_slug_fr = models.CharField(verbose_name=_('french right slug name'),max_length=200, unique=True)
    whytab_right_slug = bilingual_field('whytab_right_slug')
    whytab_right_icon = models.ImageField(verbose_name=_('rightside icon'), upload_to='whytabs/', default='placeholders/50x50.gif', blank=False)
    whytab_icon = bilingual_field('whytab_icon')
    whytab_order = models.IntegerField(verbose_name=_('order'), unique=False, blank=True, null=True)

    class Meta:
        verbose_name = _('whytab')
        verbose_name_plural = _('whytabs')
        ordering = ['whytab_order']

    def __str__(self):
        return self.whytab_class_name

    def is_default(self, this, field):
        return self._meta.get_field(field).get_default() == str(getattr(this, field))

    def clean_whytab_icon(self):
        try:
            this = Whytab.objects.get(whytab_id=self.whytab_id)
            if not self.is_default(this, 'whytab_left_icon') and this.whytab_left_icon != self.whytab_left_icon:
                this.whytab_left_icon.storage.delete(this.whytab_left_icon.path)
            if not self.is_default(this, 'whytab_right_icon') and this.whytab_right_icon != self.whytab_right_icon:
                this.whytab_right_icon.storage.delete(this.whytab_right_icon.path)
        except: pass

    def admin_whytab_left_icon(self):
        return '<img src="%s" width="100px"/>' % self.whytab_left_icon.url

    admin_whytab_left_icon.short_description = _('left icon preview')
    admin_whytab_left_icon.allow_tags = True

    def admin_whytab_right_icon(self):
        return '<img src="%s" width="100px"/>' % self.whytab_right_icon.url

    admin_whytab_right_icon.short_description = _('right icon preview')
    admin_whytab_right_icon.allow_tags = True

    def save(self, *args, **kwargs):
        self.clean_whytab_icon()
        super(Whytab, self).save(*args, **kwargs)