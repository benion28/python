from rest_framework import serializers
from .models import CustomUser

# CustomUserSerializer
class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model.
    """
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'creator_id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
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
            'date_joined',
            'updated_at'
        ]
        extra_kwargs = {
            'password1': {'write_only': True},
            'password2': {'write_only': True},
            'creator_id': {'read_only': True},
            'date_joined': {'read_only': True},
            'updated_at': {'read_only': True}
        }
        read_only_fields = ['id', 'creator_id', 'date_joined', 'updated_at']
