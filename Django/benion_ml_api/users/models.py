from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings  # To reference the AUTH_USER_MODEL for ForeignKey


# Create your models here.
class CustomUser(AbstractUser):
    """
    Custom User model extending AbstractUser to include ML-specific fields.
    Fields already in AbstractUser: username, first_name, last_name, email, password,
                                   is_staff, is_active, is_superuser, last_login, date_joined.
    """

    # --- Choices ---
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
        ('ai-developer', 'AI Developer'),
    ]
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('suspended', 'Suspended'),
    ]
    THEME_CHOICES = [
        ('light', 'Light'),
        ('dark', 'Dark'),
        # Add other themes if needed
    ]

    # --- Additional Fields ---
    # birthday: Maps to DateField. Allow null and blank.
    birthday = models.DateField(null=True, blank=True)

    # gender: CharField with choices and default.
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default='other'
    )

    # role: CharField with choices and default.
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='user'
    )

    # status: CharField with choices. AbstractUser has `is_active` (Boolean),
    # but schema has 'active'/'suspended'. We can add this field separately.
    # Or, you could potentially override `is_active` logic if preferred,
    # but adding a separate 'status' field is simpler.
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active'
    )

    # profileImage: Split into URL and public ID. Allow null and blank.
    profile_image_url = models.URLField(max_length=500, null=True, blank=True)
    profile_image_public_id = models.CharField(max_length=200, null=True, blank=True)

    # languagePreference: Simple CharField with default.
    language_preference = models.CharField(max_length=10, default='en')

    # theme: CharField with choices and default.
    theme = models.CharField(
        max_length=10,
        choices=THEME_CHOICES,
        default='light'
    )

    # apiUsage: IntegerField with default.
    api_usage = models.IntegerField(default=0)

    # modelPreferences: JSONField to store a list of strings.
    model_preferences = models.JSONField(default=list, blank=True)  # list for empty JSON array

    # trainingData: JSONField to store a list of strings (or identifiers).
    # Consider if this should relate to another model if these are complex objects.
    training_data = models.JSONField(default=list, blank=True)  # list for empty JSON array

    # personalizationSettings: JSONField to store arbitrary key-value pairs.
    personalization_settings = models.JSONField(default=dict, blank=True)  # dict for empty JSON object

    # twoFactorEnabled: BooleanField with default.
    two_factor_enabled = models.BooleanField(default=False)

    # dataSharingConsent: BooleanField with default.
    data_sharing_consent = models.BooleanField(default=True)

    # creatorId: ForeignKey to self. Optional relationship.
    # Use settings.AUTH_USER_MODEL to correctly reference the user model.
    # on_delete=models.SET_NULL means if the creator user is deleted,
    # this field becomes NULL. Adjust if different behavior is needed (e.g., PROTECT).
    creator_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_users'  # Avoids clash with default user relations
    )

    # updatedAt: DateTimeField that automatically updates on save.
    # `date_joined` from AbstractUser covers `createdAt`.
    updated_at = models.DateTimeField(auto_now=True)

    # --- Meta Options ---
    # If you need additional meta options, add them here
    # class Meta:
    #     verbose_name = 'ML User'
    #     verbose_name_plural = 'ML Users'

    # --- String Representation ---
    def __str__(self):
        # Customize how the user object is represented as a string
        return f"{self.first_name} {self.last_name} ({self.username})"
