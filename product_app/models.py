from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)


    def __str__(self):
        return self.name
