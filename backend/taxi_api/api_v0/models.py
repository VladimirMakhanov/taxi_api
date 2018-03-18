from django.db import models

# Create your models here.


class Client(models.Model):
    """
    Model representing a unique user
    """

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Driver(models.Model):
    """
    Model representing a unique driver. Looks like client, and maybe right way is combine them.
    But if develop this API -- they'll be different.
    """

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


