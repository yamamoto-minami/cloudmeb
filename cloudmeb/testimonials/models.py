from django.db import models
from cloudmeb.solutions.models import Solution
from cloudmeb.utils.i18n import bilingual_field
from django.utils.translation import ugettext_lazy as _

TESTIMONIAL_TYPES = (
	('CLIENT', _('Client')),
	('PARTNER', _('Partner')),
)

class Testimonial(models.Model):
        testimonial_id = models.AutoField(primary_key=True)
        testimonial_type = models.CharField(verbose_name=_('type'), max_length=100, choices=TESTIMONIAL_TYPES)
        testimonial_full_name = models.CharField(verbose_name=_('full name'), max_length=200, unique=False)
        testimonial_company_name_en = models.CharField(verbose_name=_('english company name'), max_length=200, unique=False)
        testimonial_company_name_fr = models.CharField(verbose_name=_('french company name'), max_length=200, unique=False)
        testimonial_company_name = bilingual_field('testimonial_company_name')
        testimonial_position_en = models.CharField(verbose_name=_('english company position'), max_length=200, unique=False)
        testimonial_position_fr = models.CharField(verbose_name=_('french company position'), max_length=200, unique=False)
        testimonial_position = bilingual_field('testimonial_position')
        testimonial_body_en = models.TextField(verbose_name=_('english body'))
        testimonial_body_fr = models.TextField(verbose_name=_('french body'))
        testimonial_body = bilingual_field('testimonial_body')
        testimonial_mugshot = models.ImageField(verbose_name=_('mugshot'), upload_to='testimonials/', default='placeholders/mugshot.png', blank=False)
        testimonial_solutions = models.ManyToManyField(Solution, verbose_name=_('solutions'))

        class Meta:
            verbose_name = _('testimonial')
            verbose_name_plural = _('testimonials')

        def __str__(self):
            return self.testimonial_full_name

        def admin_testimonial_mugshot(self):
            return '<img style="background: #f7f7f7;" src="%s" width="100px"/>' % self.testimonial_mugshot.url

        admin_testimonial_mugshot.short_description = _('mugshot preview')
        admin_testimonial_mugshot.allow_tags = True

        def admin_testimonial_solutions(self):
            return '<ul>%s</ul>' % ''.join(['<li>%s</li>' % solution for solution in self.testimonial_solutions.all()])

        admin_testimonial_solutions.short_description = _('values')
        admin_testimonial_solutions.allow_tags = True

        def is_default(self, this, field):
            return self._meta.get_field(field).get_default() == str(getattr(this, field))

        def clean_testimonial_media(self):
            try:
                this = Testimonial.objects.get(testimonial_id=self.testimonial_id)
                if not self.is_default(this, 'testimonial_mugshot') and this.testimonial_mugshot != self.testimonial_mugshot:
                     this.testimonial_mugshot.storage.delete(this.testimonial_mugshot.path)
            except: pass

        def save(self, *args, **kwargs):
            self.clean_testimonial_media()
            super(Testimonial, self).save(*args, **kwargs)
