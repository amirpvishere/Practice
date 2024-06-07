from django.db import models


class Account(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=18)
    last_name = models.CharField(max_length=32)
    age = models.IntegerField()
    city = models.CharField(max_length=15)
    image = models.ImageField(null=True, upload_to="Accounts")

    def __str__(self):
        return self.username


