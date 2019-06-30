from django.db import models
import datetime


class User(models.Model):
    user_name = models.CharField(max_length=100)
    dateOfBirth = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.user_name
