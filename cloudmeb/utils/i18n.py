from django.utils.translation import get_language
from django.conf import settings

def bilingual_field_name(self, name):
	return '_'.join((name, get_language()[:2]))

def bilingual_name(self, name, default=settings.LANGUAGE_CODE[:2]):
	lang = get_language()[:2]
	try:
		return getattr(self, '_'.join((name, lang)))
	except AttributeError:
		return getattr(self, '_'.join((name, default)))

def bilingual_field(name):

	@property
	def i18n_field_getter(self):
		return bilingual_name(self, name)

	return i18n_field_getter
