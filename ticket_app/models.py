from django.db import models


class Ticket(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=50)
    snumber = models.IntegerField(null=True)


    def __str__(self):
        return self.fname


