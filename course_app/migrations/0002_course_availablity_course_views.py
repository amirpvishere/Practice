# Generated by Django 5.0.5 on 2024-05-23 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='availablity',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='course',
            name='views',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]