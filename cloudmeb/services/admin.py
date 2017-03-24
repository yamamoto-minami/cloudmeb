from django.contrib import admin
from cloudmeb.services.models import Service
from cloudmeb.solutions.admin import SolutionAdmin
from cloudmeb.pages.admin import PageAdmin
from django.utils.translation import ugettext_lazy as _

class ServiceAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Basic'), {
            'fields': SolutionAdmin.info + ('service_order',)
        }),
        (_('Page'), {
            'fields': PageAdmin.fields
        }),
        (_('Media'), {
            'fields': SolutionAdmin.medias
        }),
        (_('Benefits'), {
            'fields': SolutionAdmin.benefits
        }),
        (_('Values'), {
            'fields': SolutionAdmin.values
        }),
        (_('Categories'), {
            'fields': SolutionAdmin.categories
        }),
    )

    list_display = SolutionAdmin.list_display + PageAdmin.list_display
    readonly_fields = SolutionAdmin.readonly_fields + PageAdmin.readonly_fields
    filter_horizontal = SolutionAdmin.filter_horizontal
    list_filter = PageAdmin.list_filter
    search_fields = SolutionAdmin.search_fields

admin.site.register(Service, ServiceAdmin)
