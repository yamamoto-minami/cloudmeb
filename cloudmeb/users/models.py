from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
	def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
		now = timezone.now()
		if not email:
			raise ValueError('The given email must be set')

		email = self.normalize_email(email)
		user = self.model(email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		return self._create_user(email, password, False, False, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		return self._create_user(email, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
	user_id = models.AutoField(primary_key=True)
	email = models.EmailField(verbose_name=_('email address'), max_length=254, unique=True)
	first_name = models.CharField(verbose_name=_('first name'), max_length=30, blank=False)
	last_name = models.CharField(verbose_name=_('last name'), max_length=30, blank=False)
	is_staff = models.BooleanField(verbose_name=_('staff status'), default=False, help_text=_('Designates whether the user can log into this admin site.'))
	is_active = models.BooleanField(verbose_name=_('active'), default=False, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
	date_joined = models.DateTimeField(verbose_name=_('date joined'), default=timezone.now)
	avatar = models.ImageField(verbose_name=_('avatar'), upload_to='users/', default='placeholders/100x100.gif', blank=False)
	slug = models.SlugField(verbose_name=_('slug'), max_length=100, unique=True, blank=True)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name']

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')

	def __str__(self):
		return self.email

	def is_default(self, this, field):
		return self._meta.get_field(field).get_default() == str(getattr(this, field))

	def clean_avatar(self):
		try:
			this = User.objects.get(user_id=self.user_id)
			if not self.is_default(this, 'avatar') and this.avatar != self.avatar:
				this.avatar.storage.delete(this.avatar.path)
		except: pass

	def admin_avatar(self):
		return '<img src="%s" width="100px"/>' % self.avatar.url

	admin_avatar.short_description = _('avatar preview')
	admin_avatar.allow_tags = True

	def get_absolute_url(self):
		return '/users/%s/' % urlquote(self.slug)

	def generate_slug(self):
		if (not self.slug):
			self.slug = slugify('%s %s' % (self.first_name, self.last_name))

	def get_full_name(self):
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		return self.first_name

	def email_user(self, subject, message, from_email=None):
		send_mail(subject, message, from_email, [self.email])

	def save(self, *args, **kwargs):
		self.clean_avatar()
		self.generate_slug()
		super(User, self).save(*args, **kwargs)
