from django.db import models
import datetime


class UserDetail(models.Model):
    user_name = models.CharField(max_length=100, primary_key=True, unique=True)
    dateOfBirth = models.DateField()

    USERNAME_FIELD = 'user_name'

    def __str__(self):
        return self.user_name
