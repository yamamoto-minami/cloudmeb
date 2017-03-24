from django.utils.translation import ugettext_lazy as _
from django.conf.urls import include, url, i18n
from django.views.i18n import javascript_catalog
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django.conf import settings
from django.contrib import admin
from cloudmeb.api import api
from cloudmeb.sitemaps import StaticSitemap, ProductSitemap, ServiceSitemap

sitemaps = {
    'static': StaticSitemap,
    'products': ProductSitemap,
    'services': ServiceSitemap
}

urlpatterns = [
    url(r'^jsi18n/$', javascript_catalog),
    url(r'^i18n/', include(i18n)),
    url(r'^api/', include(api.urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^salesforce/', 'cloudmeb.pages.views.salesforce', name='salesforce'),
    url(r'^email/', 'cloudmeb.pages.views.email', name='email'),
    url(r'^emailsec/', 'cloudmeb.pages.views.emailsec', name='emailsec'),
]

urlpatterns += i18n.i18n_patterns(
    url(r'^$', RedirectView.as_view(pattern_name='why_cloudmeb')),
    url(_(r'^admin/'), include(admin.site.urls)),
    url(_(r'^why-cloudmeb/'), 'cloudmeb.pages.views.why_cloudmeb', name='why_cloudmeb'),
    url(_(r'^book-now/'), 'cloudmeb.pages.views.book_now', name='book_now'),
    url(_(r'^pricing/'), 'cloudmeb.pages.views.pricing', name='pricing'),
    url(_(r'^frequently-asked-questions/'), 'cloudmeb.pages.views.frequently_asked_questions', name='frequently_asked_questions'),
    url(_(r'^contact-us/'), 'cloudmeb.pages.views.contact_us', name='contact_us'),
    url(_(r'^terms-of-use/'), 'cloudmeb.pages.views.terms_of_use', name='terms_of_use'),
    url(_(r'^privacy-policy/'), 'cloudmeb.pages.views.privacy_policy', name='privacy_policy'),
    url(_(r'^solutions/'), 'cloudmeb.pages.views.solutions', name='solutions'),
    url(_(r'^become-a-partner/'), 'cloudmeb.pages.views.become_a_partner', name='become_a_partner'),
    url(_(r'^plug-in-your-business/'), 'cloudmeb.pages.views.plug_in_your_business', name='plug_in_your_business'),
    url(_(r'^products/(?P<slug>[^\.]+)/'), 'cloudmeb.pages.views.product', name='products'),
    url(_(r'^services/(?P<slug>[^\.]+)/'), 'cloudmeb.pages.views.service', name='services'),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
