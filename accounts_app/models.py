from django.db import models


class Account(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=18)
    last_name = models.CharField(max_length=32)
    age = models.IntegerField(max_length=3)
    city = models.CharField(max_length=15)

    def __str__(self):
        return self.username


