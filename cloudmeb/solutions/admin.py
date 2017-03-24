from django.contrib import admin
from cloudmeb.solutions.models import Solution
from cloudmeb.pages.models import Page
from django.utils.translation import ugettext_lazy as _

class SolutionAdmin(admin.ModelAdmin):
	info = ('solution_name_en', 'solution_name_fr', 'solution_tagline_en', 'solution_tagline_fr', 'solution_slug_en', 'solution_slug_fr', 'solution_description_en', 'solution_description_fr', 'solution_medium_description_en', 'solution_medium_description_fr', 'solution_short_description_en', 'solution_short_description_fr',)
	medias = ('admin_solution_image_en', 'solution_image_en', 'admin_solution_image_fr', 'solution_image_fr', 'admin_solution_banner_en', 'solution_banner_en', 'admin_solution_banner_fr', 'solution_banner_fr', 'admin_solution_icon_en', 'solution_icon_en', 'admin_solution_icon_fr', 'solution_icon_fr', 'admin_solution_logo_en', 'solution_logo_en', 'admin_solution_logo_fr', 'solution_logo_fr',)
	benefits = ('solution_benefits',)
	values = ('solution_values',)
	categories = ('solution_categories',)
	fieldsets = (
		(_('Basic'), {
			'fields': info
		}),
		(_('Media'), {
			'fields': medias
		}),
		(_('Benefits'), {
			'fields': benefits
		}),
		(_('Values'), {
			'fields': values
		}),
		(_('Categories'), {
			'fields': categories
		}),
	)
	list_display = ('solution_name_en', 'solution_name_fr', 'solution_tagline_en', 'solution_tagline_fr', 'solution_slug_en', 'solution_slug_fr', 'solution_description_en', 'solution_description_fr', 'solution_medium_description_en', 'solution_medium_description_fr', 'solution_short_description_en', 'solution_short_description_fr', 'admin_solution_image_en', 'admin_solution_image_fr', 'admin_solution_banner_en', 'admin_solution_banner_fr', 'admin_solution_icon_en', 'admin_solution_icon_fr', 'admin_solution_logo_en', 'admin_solution_logo_fr', 'admin_solution_benefits', 'admin_solution_categories', 'admin_solution_values',)
	readonly_fields = ('admin_solution_image_en', 'admin_solution_image_fr', 'admin_solution_logo_en', 'admin_solution_logo_fr', 'admin_solution_icon_en', 'admin_solution_icon_fr', 'admin_solution_banner_en', 'admin_solution_banner_fr', 'admin_solution_benefits', 'admin_solution_categories', 'admin_solution_values',)
	filter_horizontal = ('solution_values', 'solution_benefits', 'solution_categories',)
	search_fields = ['solution_name_en', 'solution_name_fr', 'solution_tagline_en', 'solution_tagline_fr', 'solution_slug_en', 'solution_slug_fr', 'solution_description_en', 'solution_description_fr', 'solution_medium_description_en', 'solution_medium_description_fr', 'solution_short_description_en', 'solution_short_description_fr',]

admin.site.register(Solution, SolutionAdmin)