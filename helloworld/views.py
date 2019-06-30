# from django.shortcuts import render
# from rest_framework.generics import get_object_or_404
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from . models import User
# from . serializers import UserSerializer

from rest_framework import generics
from rest_framework.generics import (UpdateAPIView)

from . import models
from . import serializers


# class UserView(APIView):
#     """
#     def get(self, request):
#         user = User.objects.all()
#         serializer = UserSerializer(user, many=True)
#         return Response({"user": serializer.data})
#     """
#
#     def get(self, request, username=None):
#         if username:
#             user = get_object_or_404(User.objects.all(), user_name=username)
#             serializer = UserSerializer(user)
#             return Response({"user": serializer.data})
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response({"users": serializer.data})
#
#     # def post(self, request):
#     #     user = request.data.get('user')
#     #
#     #     # Create an article from the above data
#     #     serializer = UserSerializer(data=user)
#     #     if serializer.is_valid(raise_exception=True):
#     #         user_saved = serializer.save()
#     #     return Response({"success": "User '{}' created successfully".format(user_saved.user_name)})
#
#     def put(self, request, user_name):
#         #saved_user = get_object_or_404(User.objects.all(), pk=pk)
#         saved_user = get_object_or_404(User.objects.all(), user_name=user_name)
#         data = request.data.get('user')
#         serializer = UserSerializer(instance=saved_user, data=data, partial=True)
#
#         if serializer.is_valid(raise_exception=True):
#             user_saved = serializer.save()
#         return Response({"success": "User '{}' updated successfully".format(user_saved.user_name)})


class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    lookup_field = 'user_name'


class UserUpdate(UpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    lookup_field = 'user_name'

    # def update(self, instance, validated_data):
    #     instance.user_name = validated_data.get('user_name', instance.user_name)
    #     print("hrllo")
    #     instance.dateOfBirth = validated_data.get('dateOfBirth', instance.dateOfBirth)
    #     print(validated_data.get('dateOfBirth'))
    #     instance.save()
    #     # return instance
    #     serializer = self.get_serializer(instance)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)
    def update(self, request, *args, **kwargs):
        serializer_data = request.data
        serializer = self.serializer_class(request.user, data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


