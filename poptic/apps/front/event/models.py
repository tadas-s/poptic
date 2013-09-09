from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(
        max_length=255
    )

    start = models.DateTimeField()

    finish = models.DateTimeField()
