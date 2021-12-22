from django.conf import settings
from django.db import models


class HomePage(models.Model):
    "Generated Model"
    body = models.TextField()
    multireligionvalsystem = models.TextField(
        null=True,
        blank=True,
    )
    multireligionval = models.TextField(
        null=True,
        blank=True,
    )
    multireligionstodet = models.TextField(
        null=True,
        blank=True,
    )
    trossamfund = models.TextField(
        null=True,
        blank=True,
    )
    orgnr = models.IntegerField(
        null=True,
        blank=True,
    )


class CustomText(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=150,
    )
