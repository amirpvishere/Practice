from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    availablity = models.BooleanField(default=True)
    views = models.IntegerField(max_length=15)

    def __str__(self):
        return self.title
    
