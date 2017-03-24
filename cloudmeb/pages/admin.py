from django.contrib import admin
from cloudmeb.pages.models import Page
from cloudmeb.seos.admin import SeoAdmin

class PageAdmin(admin.ModelAdmin):
    fields = ('page_name',) + SeoAdmin.fields
    list_display = ('page_name',) + SeoAdmin.list_display
    readonly_fields = SeoAdmin.readonly_fields
    list_filter = ('page_name',) + SeoAdmin.list_filter
#    search_fields = []

admin.site.register(Page, PageAdmin)
