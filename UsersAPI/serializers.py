from rest_framework import serializers
from users.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'full_name', 'phone', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            phone=validated_data['phone'],
            password=validated_data['password'],
            is_active=False
        )
        return user
