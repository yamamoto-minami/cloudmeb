from django.contrib import admin
from cloudmeb.testimonials.models import Testimonial
from django.utils.translation import ugettext_lazy as _

class TestimonialAdmin(admin.ModelAdmin):
	fieldsets = (
		(_('Basic'), {
			'fields': ('testimonial_type', 'testimonial_full_name', 'testimonial_company_name_en', 'testimonial_company_name_fr', 'testimonial_position_en', 'testimonial_position_fr', 'testimonial_body_en', 'testimonial_body_fr', 'admin_testimonial_mugshot', 'testimonial_mugshot',)
		}),
		(_('Solutions'), {
			'fields': ('testimonial_solutions',)
		}),
	)
	list_display = ('testimonial_full_name', 'testimonial_company_name', 'testimonial_position', 'testimonial_body', 'testimonial_type', 'admin_testimonial_mugshot', 'admin_testimonial_solutions',)
	readonly_fields = ('admin_testimonial_mugshot', 'admin_testimonial_solutions', )
	filter_horizontal = ('testimonial_solutions',)
	list_filter = ('testimonial_type',)
	search_fields = ['testimonial_full_name', 'testimonial_company_name', 'testimonial_position', 'testimonial_body',]

admin.site.register(Testimonial, TestimonialAdmin)