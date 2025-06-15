from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'username',
                    'password1',
                    'password2',
                    'first_name',
                    'last_name',
                    'email',
                    'birthday',
                    'gender',
                    'status',
                    'profile_image_url',
                    'profile_image_public_id',
                    'language_preference',
                    'theme',
                    'api_usage',
                    'model_preferences',
                    'training_data',
                    'personalization_settings',
                    'two_factor_enabled',
                    'data_sharing_consent',
                    'creator_id',
                    'date_joined',
                    'updated_at'
                )
            }
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
