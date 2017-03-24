from django.contrib import admin
from cloudmeb.solution_page_txts.models import Solution_page_txt
from django.utils.translation import ugettext_lazy as _

class Solution_page_txtAdmin(admin.ModelAdmin):
    fileds = ('solution_page_txt_name', 'solution_page_txt_header_title_en', 'solution_page_txt_header_title_fr', 'solution_page_txt_header_subtitle_en', 'solution_page_txt_header_subtitle_fr', 'solution_page_txt_product_title_en', 'solution_page_txt_product_title_fr', 'solution_page_txt_service_title_en', 'solution_page_txt_service_title_fr', 'solution_page_txt_cta_text_en', 'solution_page_txt_cta_text_fr',)
    list_display = ('solution_page_txt_name', 'solution_page_txt_header_title_en', 'solution_page_txt_header_title_fr', 'solution_page_txt_header_subtitle_en', 'solution_page_txt_header_subtitle_fr', 'solution_page_txt_product_title_en', 'solution_page_txt_product_title_fr', 'solution_page_txt_service_title_en', 'solution_page_txt_service_title_fr', 'solution_page_txt_cta_text_en', 'solution_page_txt_cta_text_fr',)

admin.site.register(Solution_page_txt, Solution_page_txtAdmin)
