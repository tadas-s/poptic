from django.db import models


class Event(models.Model):
    name = models.CharField(
        "event name",
        max_length=255
    )

    description = models.TextField(
        "event description"
    )

    start = models.DateTimeField(
        "start date and time"
    )

    finish = models.DateTimeField(
        "finish date and time"
    )


class Ticket(models.Model):
    name = models.CharField(
        "ticket name",
        max_length=255
    )

    description = models.TextField(
        "ticket description"
    )

    quantity = models.IntegerField(
        "quantity to sell"
    )

    event = models.ForeignKey(
        Event,
        verbose_name="Event"
    )