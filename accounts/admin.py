from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Profile

# Register your models here.
class CustomUserAdmin(UserAdmin):	
	readonly_fields = ('profile', )
	fieldsets = (
		(None, {
			'fields': ('username', 'password')
		}),
		('Personal info', {
			'fields': ('first_name', 'last_name', 'email')
		}),
		('Staff Page', {
			'fields': (
				"goes_on_staff_page", "profile"
			)
		}),
		('Permissions', {
			'fields': (
				'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'
			)
		}),
		('Important dates', {
			'fields': ('last_login', 'date_joined')
		})
	)

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('job_title','display_name')
	search_fields = ['job_title', 'display_name']

	fieldsets = [
		("", {
			'fields': (
				'job_title', 'small_profile_pic', 'headshot', 'description',
			)
		})
	]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(CustomUser, CustomUserAdmin)