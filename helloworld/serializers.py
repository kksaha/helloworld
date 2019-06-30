from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('user_name', 'dateOfBirth')
        model = models.User

    def update(self, instance, validated_data):
        instance.user_name = validated_data.get('user_name', instance.user_name)
        print("hrllo")
        instance.dateOfBirth = validated_data.get('dateOfBirth', instance.dateOfBirth)
        print(validated_data.get('dateOfBirth'))
        instance.save()
        # return instance
        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)