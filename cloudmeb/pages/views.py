from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings
from cloudmeb.products.models import Product
from cloudmeb.websites.models import Website
from cloudmeb.pages.models import Page
from cloudmeb.partner_services.models import PartnerService
from cloudmeb.services.models import Service
from cloudmeb.inputs.models import Input
from cloudmeb.values.models import Value
from cloudmeb.categories.models import Category
from cloudmeb.testimonials.models import Testimonial
from cloudmeb.experiences.models import Experience
from cloudmeb.whytabs.models import Whytab
from cloudmeb.why_cloudmeb_txts.models import Why_cloudmeb_txt
from cloudmeb.solution_page_txts.models import Solution_page_txt
from cloudmeb.become_partner_txts.models import Become_partner_txt
from cloudmeb.pricing_txts.models import Pricing_txt
from cloudmeb.shared_txts.models import Shared_txt
from django.http import Http404
from django.utils.translation import get_language
from collections import OrderedDict
from django.core.mail import send_mail, get_connection, EmailMessage
from cloudmeb.utils.crypt import decode_AES
from django.views.decorators.http import require_http_methods
import urllib
import re


def get_base_url(request):
    return '%s://%s' %(request.scheme, request.get_host())

def get_solutions_by_category(models):
    objects = dict()
    for model in models:
        try:
            solution_categories = model.solution_categories.all()
        except AttributeError:
            solution_categories = model.partner_service_service.solution_categories.all()
        for category in solution_categories:
            if (not category.category_name in objects):
                objects[category.category_name] = list()
            objects[category.category_name].append(model)
    return OrderedDict(sorted(objects.items()))

@require_http_methods(['POST'])
def salesforce(request):
    website = Website.objects.get(website_id=settings.SITE_ID)
    url = 'https://www.salesforce.com/servlet/servlet.WebToLead?encoding=UTF-8'
    data = request.POST.copy()
    data['oid'] = website.salesforce_id
    params = data.urlencode()
    request = urllib.request.urlopen(url, params.encode('utf-8'))
    status = request.status
    request.close()
    return HttpResponse(status)

@require_http_methods(['POST'])
def email(request):
    status = 0
    data = request.POST
    if all (key in data for key in ('subject', 'message', 'fname', 'email')):
        website = Website.objects.get(website_id=settings.SITE_ID)
        connection = get_connection(backend='django.core.mail.backends.smtp.EmailBackend', host=re.sub('^https?://', '', website.smtp_server), port=website.smtp_port, username=website.smtp_user, password=decode_AES(website.smtp_password), use_tls=website.smtp_tls) 
        status = EmailMessage(data.get('subject'), data.get('message'), '%s <%s>' % ('Cloudmeb server', website.smtp_from_email), ['%s <%s>' % ('Cloudmeb admin', website.smtp_from_email)], [], connection=connection, reply_to=['%s %s <%s>' % (data.get('fname'), '', data.get('email'))]).send()
    return HttpResponse(status)

@require_http_methods(['POST'])
def emailsec(request):
    status = 0
    data = request.POST
    if all (key in data for key in ('company', 'phone', 'fname', 'email')):
        website = Website.objects.get(website_id=settings.SITE_ID)
        connection = get_connection(backend='django.core.mail.backends.smtp.EmailBackend', host=re.sub('^https?://', '', website.smtp_server), port=website.smtp_port, username=website.smtp_user, password=decode_AES(website.smtp_password), use_tls=website.smtp_tls)
        status = EmailMessage(data.get('company'), data.get('phone'), '%s <%s>' % ('Cloudmeb server', website.smtp_from_email), ['%s <%s>' % ('Cloudmeb admin', website.smtp_from_email)], [], connection=connection, reply_to=['%s %s <%s>' % (data.get('fname'), '', data.get('email'))]).send()
    return HttpResponse(status)

@ensure_csrf_cookie
def why_cloudmeb(request):
    return render_to_response('why_cloudmeb.html', {
        'base_url': get_base_url(request),
        'page': Page.objects.get(page_name='WHY_CLOUDMEB'),
        'website': Website.objects.get(website_id=settings.SITE_ID),
        'products': Product.objects.order_by('product_order').all(),
        'testimonials': Testimonial.objects.filter(testimonial_type='CLIENT'),
        'experiences': Experience.objects.all(),
        'whytabs': Whytab.objects.all(),
        'why_cloudmeb_txt': Why_cloudmeb_txt.objects.get(why_cloudmeb_txt_name='WHY_CLOUDMEB'),
        'services': Service.objects.order_by('service_order').all(),
        'shared_txts': Shared_txt.objects.all(),
    }, context_instance = RequestContext(request))

@ensure_csrf_cookie
def book_now(request):
    return render_to_response('book_now.html', {
        'base_url': get_base_url(request),
        'page': Page.objects.get(page_name='BOOK_NOW'),
        'website': Website.objects.get(website_id=settings.SITE_ID),
        'services': Service.objects.order_by('service_order').all()
    }, context_instance = RequestContext(request))

@ensure_csrf_cookie
def contact_us(request):
    return render_to_response('contact_us.html', {
        'base_url': get_base_url(request),
        'page': Page.objects.get(page_name='CONTACT_US'),
        'website': Website.objects.get(website_id=settings.SITE_ID),
        'services': Service.objects.order_by('service_order').all(),
        'shared_txts': Shared_txt.objects.all(),
    }, context_instance = RequestContext(request))

@ensure_csrf_cookie
def frequently_asked_questions(request):
    return render_to_response('frequently_asked_questions.html', {
        'base_url': get_base_url(request),
        'page': Page.objects.get(page_name='FREQUENTLY_ASKED_QUESTIONS'),
        'website': Website.objects.get(website_id=settings.SITE_ID),
        'services': Service.objects.order_by('service_order').all(),
        'shared_txts': Shared_txt.objects.all(),
    }, context_instance = RequestContext(request))

@ensure_csrf_cookie
def plug_in_your_business(request):
    partner_services = PartnerService.objects.order_by('partner_service_service__service_order').all()
    products = Product.objects.order_by('product_order').all()
    solutions_length = len(partner_services) + len(products)
    return render_to_response('plug_in_your_business.html', {
        'base_url': get_base_url(request),
        'page': Page.objects.get(page_name='PLUG_IN_YOUR_BUSINESS'),
        'website': Website.objects.get(website_id=settings.SITE_ID),
        'inputs': Input.objects.order_by('input_order').all(),
        'solutions_length': solutions_length,
        'products': products,
        'partner_services': partner_services,
        'product_categories': get_solutions_by_category(products),
        'service_categories': get_solutions_by_category(partner_services),
        'services': Service.objects.order_by('service_order').all(),
        'pricing_txt': Pricing_txt.objects.get(Pricing_txt_name='PLUG_IN_YOUR_BUSINESS'),
        'shared_txts': Shared_txt.objects.all(),
    }, context_instance = RequestContext(request))

@ensure_csrf_cookie
def pricing(request):
    return render_to_response('pricing.html', {
        'base_url': get_base_url(request),
        'page': Page.objects.get(page_name='PRICING'),
        'website': Website.objects.get(website_id=settings.SITE_ID),
        'services': Service.objects.order_by('service_order').all(),
        'shared_txts': Shared_txt.objects.all(),
    }, context_instance = RequestContext(request))

@ensure_csrf_cookie
def solutions(request):
    return render_to_response('solutions.html', {
        # 'partners': Partner.objects.all(),
        'base_url': get_base_url(request),
        'page': Page.objects.get(page_name='SOLUTIONS'),
        'website': Website.objects.get(website_id=settings.SITE_ID),
        'products': Product.objects.order_by('product_order').all(),
        'services': Service.objects.order_by('service_order').all(),
        'solution_page_txt': Solution_page_txt.objects.get(solution_page_txt_name='SOLUTIONS'),
        'shared_txts': Shared_txt.objects.all(),
    }, context_instance = RequestContext(request))

@ensure_csrf_cookie
def product(request, slug):
    try:
        if (get_language()[:2] == 'en'):
            model = Product.objects.get(solution_slug_en=slug)
        else:
            model = Product.objects.get(solution_slug_fr=slug)

        return render_to_response('product.html', {
            'base_url': get_base_url(request),
            'website': Website.objects.get(website_id=settings.SITE_ID),
            'page': model,
            'product': model,
            'services': Service.objects.order_by('service_order').all(),
            'shared_txts': Shared_txt.objects.all(),
        }, context_instance = RequestContext(request))

    except Product.DoesNotExist:
        raise Http404()

@ensure_csrf_cookie
def service(request, slug):
    try:
        if (get_language()[:2] == 'en'):
            model = Service.objects.get(solution_slug_en=slug)
        else:
            model = Service.objects.get(solution_slug_fr=slug)

        return render_to_response('service.html', {
            'base_url': get_base_url(request),
            'website': Website.objects.get(website_id=settings.SITE_ID),
            'page': model,
            'service': model,
            'services': Service.objects.order_by('service_order').all(),
            'shared_txts': Shared_txt.objects.all(),
        }, context_instance = RequestContext(request))

    except Service.DoesNotExist:
        raise Http404()

# @ensure_csrf_cookie
# def partner(request, slug):
#     return render_to_response('partner.html', {
#         'partner': get_object_or_404(Partner, slug=slug),
#         'services': Service.objects.order_by('service_order').all(),
#     }, context_instance = RequestContext(request))

@ensure_csrf_cookie
def become_a_partner(request):
    return render_to_response('become_a_partner.html', {
        'base_url': get_base_url(request),
        'website': Website.objects.get(website_id=settings.SITE_ID),
        'page': Page.objects.get(page_name='BECOME_A_PARTNER'),
        'products': Product.objects.order_by('product_order').all(),
        'services': Service.objects.order_by('service_order').all(),
        'become_partner_txt': Become_partner_txt.objects.get(become_partner_txt_name='BECOME_A_PARTNER'),
        'shared_txts': Shared_txt.objects.all(),
        'testimonials': Testimonial.objects.filter(testimonial_type='PARTNER')
    }, context_instance = RequestContext(request))

@ensure_csrf_cookie
def terms_of_use(request):
    return render_to_response('terms_of_use.html', {
        'base_url': get_base_url(request),
        'page': Page.objects.get(page_name='TERMS_OF_USE'),
        'website': Website.objects.get(website_id=settings.SITE_ID),
        'services': Service.objects.order_by('service_order').all(),
        'shared_txts': Shared_txt.objects.all(),
    }, context_instance = RequestContext(request))

@ensure_csrf_cookie
def privacy_policy(request):
    return render_to_response('privacy_policy.html', {
        'base_url': get_base_url(request),
        'page': Page.objects.get(page_name='PRIVACY_POLICY'),
        'website': Website.objects.get(website_id=settings.SITE_ID),
        'services': Service.objects.order_by('service_order').all(),
        'shared_txts': Shared_txt.objects.all(),
    }, context_instance = RequestContext(request))
