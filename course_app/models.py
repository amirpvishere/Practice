from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    availablity = models.BooleanField(default=True)
    views = models.IntegerField(null=True)
    image = models.ImageField(null=True, upload_to="Courses")

    def __str__(self):
        return self.title
    
