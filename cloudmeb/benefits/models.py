from django.db import models
from cloudmeb.utils.i18n import bilingual_field, bilingual_name
from django.utils.translation import ugettext_lazy as _

class Benefit(models.Model):
	benefit_id = models.AutoField(primary_key=True)
	benefit_name_en = models.CharField(verbose_name=_('english name'), max_length=200, unique=True)
	benefit_name_fr = models.CharField(verbose_name=_('french name'),max_length=200, unique=True)
	benefit_name = bilingual_field('benefit_name')
	benefit_short_name_en = models.CharField(verbose_name=_('english short name'), max_length=100, unique=True)
	benefit_short_name_fr = models.CharField(verbose_name=_('french short name'), max_length=100, unique=True)
	benefit_short_name = bilingual_field('benefit_short_name')
	benefit_description_en = models.TextField(verbose_name=_('english description'), max_length=1000, unique=True)
	benefit_description_fr = models.TextField(verbose_name=_('french description'), max_length=1000, unique=True)
	benefit_description = bilingual_field('benefit_description')
	benefit_medium_description_en = models.TextField(verbose_name=_('english medium description'), max_length=500, unique=True)
	benefit_medium_description_fr = models.TextField(verbose_name=_('french medium description'), max_length=500, unique=True)
	benefit_medium_description = bilingual_field('benefit_medium_description')
	benefit_short_description_en = models.TextField(verbose_name=_('english short description'), max_length=250, unique=True)
	benefit_short_description_fr = models.TextField(verbose_name=_('french short description'), max_length=250, unique=True)
	benefit_short_description = bilingual_field('benefit_short_description')
	benefit_image_en = models.ImageField(verbose_name=_('english image'), upload_to='benefits/', default='placeholders/300x300.gif', blank=False)
	benefit_image_fr = models.ImageField(verbose_name=_('french image'), upload_to='benefits/', default='placeholders/300x300.gif', blank=False)
	benefit_image = bilingual_field('benefit_image')
	benefit_order = models.IntegerField(verbose_name=_('order'), unique=False, blank=True, null=True)

	class Meta:
		verbose_name = _('benefit')
		verbose_name_plural = _('benefits')
		ordering = ['benefit_order']

	def __str__(self):
		return self.benefit_name

	def is_default(self, this, field):
		return self._meta.get_field(field).get_default() == str(getattr(this, field))

	def clean_benefit_image(self):
		try:
			this = Benefit.objects.get(benefit_id=self.benefit_id)
			if not self.is_default(this, 'benefit_image_en') and this.benefit_image_en != self.benefit_image_en:
				this.benefit_image_en.storage.delete(this.benefit_image_en.path)
			if not self.is_default(this, 'benefit_image_fr') and this.benefit_image_fr != self.benefit_image_fr:
				this.benefit_image_fr.storage.delete(this.benefit_image_fr.path)
		except: pass

	def admin_benefit_image_en(self):
		return '<img src="%s" width="100px"/>' % self.benefit_image_en.url

	admin_benefit_image_en.short_description = _('english image preview')
	admin_benefit_image_en.allow_tags = True

	def admin_benefit_image_fr(self):
		return '<img src="%s" width="100px"/>' % self.benefit_image_fr.url

	admin_benefit_image_fr.short_description = _('french image preview')
	admin_benefit_image_fr.allow_tags = True

	def admin_benefit_image(self):
		return bilingual_name(self, 'admin_benefit_image')()

	admin_benefit_image.short_description = _('image preview')
	admin_benefit_image.allow_tags = True

	def save(self, *args, **kwargs):
		self.clean_benefit_image()
		super(Benefit, self).save(*args, **kwargs)
