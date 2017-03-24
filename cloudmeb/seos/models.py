from django.db import models
from cloudmeb.utils.i18n import bilingual_field, bilingual_name, bilingual_field_name
from django.utils.translation import ugettext_lazy as _

TYPES = (
	('WEBSITE', _('Website')),
	('ARTICLE', _('Article')),
)

class Seo(models.Model):
	seo_id = models.AutoField(primary_key=True)
	seo_type = models.CharField(verbose_name=_('seo type'), max_length=100, choices=TYPES)
	seo_image_en = models.ImageField(verbose_name=_('english seo image'), upload_to='seos/', default='placeholders/300x300.gif', blank=False)
	seo_image_fr = models.ImageField(verbose_name=_('french seo image'), upload_to='seos/', default='placeholders/300x300.gif', blank=False)
	seo_image = bilingual_field('seo_image')
	seo_meta_title_en = models.CharField(verbose_name=_('english meta title'), max_length=60, unique=True)
	seo_meta_title_fr = models.CharField(verbose_name=_('french meta title'), max_length=60, unique=True)
	seo_meta_title = bilingual_field('seo_meta_title')
	seo_meta_description_en = models.TextField(verbose_name=_('english meta description'), max_length=155, unique=True)
	seo_meta_description_fr = models.TextField(verbose_name=_('french meta description'), max_length=155, unique=True)
	seo_meta_description = bilingual_field('seo_meta_description')
	seo_meta_keywords_en = models.TextField(verbose_name=_('english meta keywords'), max_length=1000, unique=True)
	seo_meta_keywords_fr = models.TextField(verbose_name=_('french meta keywords'), max_length=1000, unique=True)
	seo_meta_keywords = bilingual_field('seo_meta_keywords')
	seo_meta_debug = models.TextField(verbose_name=_('debug'), default='debug')

	class Meta:
		verbose_name = _('seo')
		verbose_name_plural = _('seos')

	def __str__(self):
		return self.seo_meta_title

	def is_default(self, this, field):
		return self._meta.get_field(field).get_default() == str(getattr(this, field))

	def is_default_seo_image(self):
		return self.is_default(self, bilingual_field_name(self, 'seo_image'))

	def clean_seo_image(self):
		try:
			this = Seo.objects.get(seo_id=self.seo_id)
			if not self.is_default(this, 'seo_image_en') and this.seo_image_en != self.seo_image_en:
				this.seo_image_en.storage.delete(this.seo_image_en.path)
			if not self.is_default(this, 'seo_image_fr') and this.seo_image_fr != self.seo_image_fr:
				this.seo_image_fr.storage.delete(this.seo_image_fr.path)
		except: pass

	def admin_seo_image_en(self):
		return '<img src="%s" width="100px"/>' % self.seo_image_en.url

	admin_seo_image_en.short_description = _('english seo image preview')
	admin_seo_image_en.allow_tags = True

	def admin_seo_image_fr(self):
		return '<img src="%s" width="100px"/>' % self.seo_image_fr.url

	admin_seo_image_fr.short_description = _('french seo image preview')
	admin_seo_image_fr.allow_tags = True

	def admin_seo_image(self):
		return bilingual_name(self, 'admin_seo_image')()

	admin_seo_image.short_description = _('seo image preview')
	admin_seo_image.allow_tags = True

	def save(self, *args, **kwargs):
		self.clean_seo_image()
		super(Seo, self).save(*args, **kwargs)
