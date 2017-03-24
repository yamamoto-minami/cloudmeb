from django.contrib import admin
from cloudmeb.experiences.models import Experience
from django.utils.translation import ugettext_lazy as _

# Register your models here.


class ExperienceAdmin(admin.ModelAdmin):
        fieldsets = (
                (_('Basic'), {
                        'fields': ('experience_class_name', 'experience_menu_tab_name_en', 'experience_menu_tab_name_fr', 'experience_body_top_en', 'experience_body_top_fr','experience_body_bottom_en', 'experience_body_bottom_fr', 'experience_background','admin_experience_background', 'experience_order',)
                }),
        )
        list_display = ('experience_class_name', 'experience_menu_tab_name', 'experience_body_top', 'experience_body_bottom', 'admin_experience_background', 'experience_order',)
        readonly_fields = ('admin_experience_background',)
        search_fields = ['experience_class_name', 'experience_menu_tab_name', 'experience_body_top', 'experience_body_bottom',]

admin.site.register(Experience, ExperienceAdmin)
