from django.contrib import sitemaps
from django.utils.translation import get_language
from django.core.urlresolvers import reverse
from cloudmeb.products.models import Product
from cloudmeb.services.models import Service

class StaticSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    i18n = True

    def items(self):
        return ['why_cloudmeb', 'pricing', 'frequently_asked_questions', 'contact_us', 'terms_of_use', 'privacy_policy', 'solutions', 'become_a_partner', 'plug_in_your_business']

    def location(self, item):
        return reverse(item)

class ProductSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    i18n = True

    def items(self):
        return Product.objects.all()

class ServiceSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    i18n = True

    def items(self):
        return Service.objects.all()
