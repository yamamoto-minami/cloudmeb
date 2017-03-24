from django.db import models
from cloudmeb.categories.models import Category
from cloudmeb.values.models import Value
from cloudmeb.benefits.models import Benefit
from cloudmeb.utils.i18n import bilingual_field
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

class Solution(models.Model):
	solution_id = models.AutoField(primary_key=True)
	solution_name_en = models.CharField(verbose_name=_('english name'), max_length=200, unique=True)
	solution_name_fr = models.CharField(verbose_name=_('french name'),max_length=200, unique=True)
	solution_name = bilingual_field('solution_name')
	solution_tagline_en = models.CharField(verbose_name=_('english tagline'), max_length=100, unique=True)
	solution_tagline_fr = models.CharField(verbose_name=_('french tagline'), max_length=100, unique=True)
	solution_tagline = bilingual_field('solution_tagline')
	solution_description_en = models.TextField(verbose_name=_('english description'))
	solution_description_fr = models.TextField(verbose_name=_('french description'))
	solution_description = bilingual_field('solution_description')
	solution_medium_description_en = models.TextField(verbose_name=_('english medium description'))
	solution_medium_description_fr = models.TextField(verbose_name=_('french medium description'))
	solution_medium_description = bilingual_field('solution_medium_description')
	solution_short_description_en = models.TextField(verbose_name=_('english short description'))
	solution_short_description_fr = models.TextField(verbose_name=_('french short description'))
	solution_short_description = bilingual_field('solution_short_description')
	solution_image_en = models.ImageField(verbose_name=_('english image'), upload_to='solutions/', default='placeholders/300x300.gif', blank=False)
	solution_image_fr = models.ImageField(verbose_name=_('french image'), upload_to='solutions/', default='placeholders/300x300.gif', blank=False)
	solution_image = bilingual_field('solution_image')
	solution_banner_en = models.ImageField(verbose_name=_('english banner'), upload_to='solutions/', default='placeholders/1600x500.gif', blank=False)
	solution_banner_fr = models.ImageField(verbose_name=_('french banner'), upload_to='solutions/', default='placeholders/1600x500.gif', blank=False)
	solution_banner = bilingual_field('solution_banner')
	solution_icon_en = models.ImageField(verbose_name=_('english icon'), upload_to='solutions/', default='placeholders/300x300.gif', blank=False)
	solution_icon_fr = models.ImageField(verbose_name=_('french icon'), upload_to='solutions/', default='placeholders/300x300.gif', blank=False)
	solution_icon = bilingual_field('solution_icon')
	solution_logo_en = models.ImageField(verbose_name=_('english logo'), upload_to='solutions/', default='placeholders/100x100.gif', blank=False)
	solution_logo_fr = models.ImageField(verbose_name=_('french logo'), upload_to='solutions/', default='placeholders/100x100.gif', blank=False)
	solution_logo = bilingual_field('solution_logo')
	solution_categories = models.ManyToManyField(Category, verbose_name=_('categories'), related_name='solutions')
	solution_values = models.ManyToManyField(Value, verbose_name=_('values'), blank=True)
	solution_benefits = models.ManyToManyField(Benefit, verbose_name=_('benefits'))
	solution_slug_en = models.SlugField(verbose_name=_('english slug'), max_length=100, unique=True, blank=True)
	solution_slug_fr = models.SlugField(verbose_name=_('french slug'), max_length=100, unique=True, blank=True)
	solution_slug = bilingual_field('solution_slug')

	class Meta:
		verbose_name = _('solution')
		verbose_name_plural = _('solutions')

	def __str__(self):
		return self.solution_name

	def is_default(self, this, field):
		return self._meta.get_field(field).get_default() == str(getattr(this, field))

	def clean_solution_media(self):
		try:
			this = Solution.objects.get(solution_id=self.solution_id)
			if not self.is_default(this, 'solution_image_en') and this.solution_image_en != self.solution_image_en:
				this.solution_image_en.storage.delete(this.solution_image_en.path)
			if not self.is_default(this, 'solution_image_fr') and this.solution_image_fr != self.solution_image_fr:
				this.solution_image_fr.storage.delete(this.solution_image_fr.path)

			if not self.is_default(this, 'solution_banner_en') and this.solution_banner_en != self.solution_banner_en:
				this.solution_banner_en.storage.delete(this.solution_banner_en.path)
			if not self.is_default(this, 'solution_banner_fr') and this.solution_banner_fr != self.solution_banner_fr:
				this.solution_banner_fr.storage.delete(this.solution_banner_fr.path)

			if not self.is_default(this, 'solution_icon_en') and this.solution_icon_en != self.solution_icon_en:
				this.solution_icon_en.storage.delete(this.solution_icon_en.path)
			if not self.is_default(this, 'solution_icon_fr') and this.solution_icon_fr != self.solution_icon_fr:
				this.solution_icon_fr.storage.delete(this.solution_icon_fr.path)

			if not self.is_default(this, 'solution_logo_en') and this.solution_logo_en != self.solution_logo_en:
				this.solution_logo_en.storage.delete(this.solution_logo_en.path)
			if not self.is_default(this, 'solution_logo_fr') and this.solution_logo_fr != self.solution_logo_fr:
				this.solution_logo_fr.storage.delete(this.solution_logo_fr.path)
		except: pass

	def admin_solution_benefits(self):
		return '<ul>%s</ul>' % ''.join(['<li>%s</li>' % benefit for benefit in self.solution_benefits.all()])

	admin_solution_benefits.short_description = _('benefits')
	admin_solution_benefits.allow_tags = True

	def admin_solution_values(self):
		return '<ul>%s</ul>' % ''.join(['<li>%s</li>' % value for value in self.solution_values.all()])

	admin_solution_values.short_description = _('values')
	admin_solution_values.allow_tags = True

	def admin_solution_categories(self):
		return '<ul>%s</ul>' % ''.join(['<li>%s</li>' % category for category in self.solution_categories.all()])

	admin_solution_categories.short_description = _('categories')
	admin_solution_categories.allow_tags = True


	def admin_solution_image_en(self):
		return '<img src="%s" width="100px"/>' % self.solution_image_en.url

	admin_solution_image_en.short_description = _('english image preview')
	admin_solution_image_en.allow_tags = True

	def admin_solution_image_fr(self):
		return '<img src="%s" width="100px"/>' % self.solution_image_fr.url

	admin_solution_image_fr.short_description = _('french image preview')
	admin_solution_image_fr.allow_tags = True

	def admin_solution_banner_en(self):
		return '<img src="%s" width="100px"/>' % self.solution_banner_en.url

	admin_solution_banner_en.short_description = _('english banner preview')
	admin_solution_banner_en.allow_tags = True

	def admin_solution_banner_fr(self):
		return '<img src="%s" width="100px"/>' % self.solution_banner_fr.url

	admin_solution_banner_fr.short_description = _('french banner preview')
	admin_solution_banner_fr.allow_tags = True

	def admin_solution_icon_en(self):
		return '<img src="%s" width="100px"/>' % self.solution_icon_en.url

	admin_solution_icon_en.short_description = _('english icon preview')
	admin_solution_icon_en.allow_tags = True

	def admin_solution_icon_fr(self):
		return '<img src="%s" width="100px"/>' % self.solution_icon_fr.url

	admin_solution_icon_fr.short_description = _('french icon preview')
	admin_solution_icon_fr.allow_tags = True

	def admin_solution_logo_en(self):
		return '<img src="%s" width="100px"/>' % self.solution_logo_en.url

	admin_solution_logo_en.short_description = _('english logo preview')
	admin_solution_logo_en.allow_tags = True

	def admin_solution_logo_fr(self):
		return '<img src="%s" width="100px"/>' % self.solution_logo_fr.url

	admin_solution_logo_fr.short_description = _('french logo preview')
	admin_solution_logo_fr.allow_tags = True

	def generate_solution_slug(self):
		if (not self.solution_slug_en):
			self.solution_slug_en = slugify(self.solution_name_en)
		if (not self.solution_slug_fr):
			self.solution_slug_fr = slugify(self.solution_name_fr)

	def save(self, *args, **kwargs):
		self.clean_solution_media()
		self.generate_solution_slug()
		super(Solution, self).save(*args, **kwargs)
