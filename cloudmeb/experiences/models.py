from django.db import models
from cloudmeb.utils.i18n import bilingual_field
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Experience(models.Model):
        experience_id = models.AutoField(primary_key=True)
        experience_class_name = models.CharField(verbose_name=_('class name'), max_length=200, unique=False)
        experience_menu_tab_name_en = models.CharField(verbose_name=_('english menu tab name'), max_length=200, unique=False)
        experience_menu_tab_name_fr = models.CharField(verbose_name=_('french menu tab name'), max_length=200, unique=False)
        experience_menu_tab_name = bilingual_field('experience_menu_tab_name')
        experience_body_top_en = models.TextField(verbose_name=_('english body top'))
        experience_body_top_fr = models.TextField(verbose_name=_('french body top'))
        experience_body_top = bilingual_field('experience_body_top')
        experience_body_bottom_en = models.TextField(verbose_name=_('english body bottom'))
        experience_body_bottom_fr = models.TextField(verbose_name=_('french body bottom'))
        experience_body_bottom = bilingual_field('experience_body_bottom')
        experience_order = models.IntegerField(verbose_name=_('order'), unique=False, blank=True, null=True)
        experience_background = models.ImageField(verbose_name=_('background'), upload_to='experiences/', default='placeholders/1600x500.gif', blank=False)

        class Meta:
                verbose_name = _('experience')
                verbose_name_plural = _('experiences')

        def __str__(self):
                return self.experience_class_name

        def admin_experience_background(self):
                return '<img style="background: #f7f7f7;" src="%s" width="100px"/>' % self.experience_background.url

        admin_experience_background.short_description = _('background preview')
        admin_experience_background.allow_tags = True

        def is_default(self, this, field):
                return self._meta.get_field(field).get_default() == str(getattr(this, field))

        def clean_experience_media(self):
                try:
                        this = Experience.objects.get(experience_id=self.experience_id)
                        if not self.is_default(this, 'experience_background') and this.experience_background != self.experience_background:
                                this.experience_background.storage.delete(this.experience_background.path)
                except: pass


        def save(self, *args, **kwargs):
                self.clean_experience_media()
                super(Experience, self).save(*args, **kwargs)
