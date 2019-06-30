from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('user_name', 'dateOfBirth')
        model = models.User

    def update(self, instance, validated_data, *args, **kwargs):
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.dateOfBirth = validated_data.get('dateOfBirth', instance.dateOfBirth)
        print(validated_data.get('dateOfBirth'))
        print(args)
        print(kwargs)
        instance.save()
        return
