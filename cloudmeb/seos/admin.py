from django.contrib import admin
from cloudmeb.seos.models import Seo

class SeoAdmin(admin.ModelAdmin):
	fields = ('seo_type', 'seo_meta_title_en', 'seo_meta_title_fr', 'seo_meta_description_en', 'seo_meta_description_fr', 'seo_meta_keywords_en', 'seo_meta_keywords_fr', 'admin_seo_image_en', 'seo_image_en', 'admin_seo_image_fr', 'seo_image_fr',)
	list_display = ('seo_type', 'seo_meta_title_en', 'seo_meta_title_fr', 'seo_meta_description_en', 'seo_meta_description_fr', 'seo_meta_keywords_en', 'seo_meta_keywords_fr', 'admin_seo_image_en', 'admin_seo_image_fr',)
	readonly_fields = ('admin_seo_image_en', 'admin_seo_image_fr',)
	list_filter = ('seo_type',)
	search_fields = ['seo_meta_title_en', 'seo_meta_title_fr', 'seo_meta_description_en', 'seo_meta_description_fr', 'seo_meta_keywords_en', 'seo_meta_keywords_fr',]

admin.site.register(Seo, SeoAdmin)
