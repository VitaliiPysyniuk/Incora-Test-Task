from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        user.save()

        return user

    def update(self, instance, validated_data):
        updated_instance = super().update(instance, validated_data)
        updated_instance.set_password(validated_data['password'])
        updated_instance.save()

        return updated_instance


