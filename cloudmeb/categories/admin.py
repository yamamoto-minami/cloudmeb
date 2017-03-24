from django.contrib import admin
from cloudmeb.categories.models import Category

class CategoryAdmin(admin.ModelAdmin):
	fields = ('category_name_en', 'category_name_fr', 'category_short_name_en', 'category_short_name_fr',)
	list_display = ('category_name_en', 'category_name_fr', 'category_short_name_en', 'category_short_name_fr',)
	search_fields = ['category_name_en', 'category_name_fr', 'category_short_name_en', 'category_short_name_fr',]

admin.site.register(Category, CategoryAdmin)