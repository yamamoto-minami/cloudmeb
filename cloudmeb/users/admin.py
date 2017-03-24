from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from tastypie.admin import ApiKeyInline
from tastypie.models import ApiAccess, ApiKey
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group
from cloudmeb.users.models import User
from cloudmeb.users.forms import UserCreationForm, UserChangeForm

class UserAdmin(BaseUserAdmin):
	basic_info = ('email', 'password',)
	personal_info = ('first_name', 'last_name', 'admin_avatar', 'avatar', 'slug',)
	permissions = ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
	important_dates = ('last_login', 'date_joined')
	fieldsets = (
		(_('Basic info'), {
			'fields': basic_info
		}),
		(_('Personal info'), {
			'fields': personal_info
		}),
		(_('Permissions'), {
			'classes': ('collapse',),
			'fields': permissions
		}),
		(_('Important dates'), {
			'fields': important_dates
		}),
	)
	add_fieldsets = (
		(_('Basic info'), {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2')
		}),
	)
	form = UserChangeForm
	add_form = UserCreationForm
	list_display = ('email', 'first_name', 'last_name', 'is_staff', 'admin_avatar', 'slug',)
	search_fields = ('email', 'first_name', 'last_name')
	readonly_fields = ('admin_avatar',)
	ordering = ('email',)
	inlines = BaseUserAdmin.inlines + [ApiKeyInline]
	list_filter = BaseUserAdmin.list_filter

admin.site.unregister(Group)
admin.site.unregister(ApiKey)
# admin.site.unregister(ApiAccess)

admin.site.register(User, UserAdmin)