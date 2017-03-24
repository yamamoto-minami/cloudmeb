from django.contrib import admin
from cloudmeb.whytabs.models import Whytab

class WhytabAdmin(admin.ModelAdmin):
    fields = ('whytab_class_name', 'whytab_menu_name_en', 'whytab_menu_name_fr', 'whytab_left_title_en', 'whytab_left_title_fr', 'whytab_left_content_en', 'whytab_left_content_fr', 'admin_whytab_left_icon', 'whytab_left_icon', 'whytab_right_title_en', 'whytab_right_title_fr', 'whytab_right_content_en', 'whytab_right_content_fr', 'whytab_right_slug_en', 'whytab_right_slug_fr', 'admin_whytab_right_icon', 'whytab_right_icon', 'whytab_order',)
    list_display = ('whytab_menu_name', 'whytab_left_title', 'whytab_left_content', 'admin_whytab_left_icon', 'whytab_right_title', 'whytab_right_content', 'whytab_right_slug', 'admin_whytab_right_icon', 'whytab_order')
    readonly_fields = ('admin_whytab_left_icon', 'admin_whytab_right_icon',)
    search_fields = ['whytab_class_name', 'whytab_menu_name_en', 'whytab_menu_name_fr', 'whytab_left_title_en', 'whytab_left_title_fr', 'whytab_left_content_en', 'whytab_left_content_fr', 'whytab_right_title_en', 'whytab_right_title_fr', 'whytab_right_content_en', 'whytab_right_content_fr', 'whytab_right_slug_en', 'whytab_right_slug_fr',]

admin.site.register(Whytab, WhytabAdmin)