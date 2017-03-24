from django.contrib import admin
from cloudmeb.shared_txts.models import Shared_txt
from django.utils.translation import ugettext_lazy as _

class Shared_txtAdmin(admin.ModelAdmin):
    fileds = ('shared_txt_name', 'shared_txt_name_en', 'shared_txt_name_fr',)
    list_display = ('shared_txt_name', 'shared_txt_name_en', 'shared_txt_name_fr',)

admin.site.register(Shared_txt, Shared_txtAdmin)  
