from django.contrib import admin
from cloudmeb.benefits.models import Benefit

class BenefitAdmin(admin.ModelAdmin):
	fields = ('benefit_name_en', 'benefit_name_fr', 'benefit_short_name_en', 'benefit_short_name_fr', 'benefit_description_en', 'benefit_description_fr', 'benefit_medium_description_en', 'benefit_medium_description_fr', 'benefit_short_description_en', 'benefit_short_description_fr', 'admin_benefit_image_en', 'benefit_image_en', 'admin_benefit_image_fr', 'benefit_image_fr', 'benefit_order',)
	list_display = ('benefit_name', 'benefit_short_name', 'benefit_description', 'benefit_medium_description', 'benefit_short_description', 'admin_benefit_image', 'benefit_order',)
	readonly_fields = ('admin_benefit_image_en', 'admin_benefit_image_fr',)
	search_fields = ['benefit_name_en', 'benefit_name_fr', 'benefit_short_name_en', 'benefit_short_name_fr', 'benefit_description_en', 'benefit_description_fr', 'benefit_medium_description_en', 'benefit_medium_description_fr', 'benefit_short_description_en', 'benefit_short_description_fr',]

admin.site.register(Benefit, BenefitAdmin)