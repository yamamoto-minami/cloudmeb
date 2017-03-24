from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from cloudmeb.utils.crypt import encode_AES, decode_AES

class Website(Site):
	website_id = models.AutoField(primary_key=True)
	smtp_user = models.EmailField(verbose_name=_('smtp user'))
	smtp_password = models.CharField(verbose_name=_('smtp password'), max_length=500)
	smtp_from_email = models.EmailField(verbose_name=_('smtp default email'))
	smtp_server = models.URLField(verbose_name=_('smtp server'))
	smtp_port = models.IntegerField(verbose_name=_('smtp port number'))
	smtp_tls = models.BooleanField(verbose_name=_('smtp use tls'))
	salesforce_id = models.CharField(verbose_name=_('salesforce id'), max_length=255)
	hotjar_id = models.CharField(verbose_name=_('hotjar id'), max_length=255)
	add_this_id = models.CharField(verbose_name=_('add this id'), max_length=255)
	facebook_pixel_id = models.CharField(verbose_name=_('facebook pixel id'), max_length=255)
	facebook_admin_id = models.CharField(verbose_name=_('facebook admin id'), max_length=255)
	bing_analytics_id = models.CharField(verbose_name=_('bing analytics id'), max_length=255)
	google_analytics_id = models.CharField(verbose_name=_('google analytics id'), max_length=255)
	google_addwords_id = models.CharField(verbose_name=_('google addwords id'), max_length=255)
	personal_google_plus_url = models.URLField(verbose_name=_('personal google plus id'))
	google_plus_url = models.URLField(verbose_name=_('google plus id'))
	twitter_url = models.URLField(verbose_name=_('twitter id'))
	facebook_url = models.URLField(verbose_name=_('facebook id'))
	linkedin_url = models.URLField(verbose_name=_('linkedin id'))
	shop_url = models.URLField(verbose_name=_('shop url'))

	class Meta:
		verbose_name = _('website')
		verbose_name_plural = _('websites')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return '/'

	def encode_smtp_password(self):
		this = None
		try:
			this = Website.objects.get(website_id=self.website_id)
		except: pass

		if (not this or this.smtp_password != self.smtp_password):
			self.smtp_password = encode_AES(self.smtp_password)

	def save(self, *args, **kwargs):
		self.encode_smtp_password()
		super(Website, self).save(*args, **kwargs)

