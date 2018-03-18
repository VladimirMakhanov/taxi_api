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


class Car(models.Model):
    """
    Model representing a car.
    """

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    driver = models.OneToOneField(
        Driver,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name}, {self.description}"


class Tariff(models.Model):
    """
    Model representing a tariff
    """

    name = models.CharField(max_length=200)
    cost_per_km = models.FloatField()

    def __str__(self):
        return f'Tariff "{self.name}", cost per km: {self.cost_per_km}'

    class Meta:
        ordering = ["cost_per_km"]


class Order(models.Model):
    """
    Model connecting clients and drivers
    """

    client = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,
        null=True,
    )
    driver = models.ForeignKey(
        Driver,
        on_delete=models.SET_NULL,
        null=True,
    )
    tariff = models.ForeignKey(
        Tariff,
        on_delete=models.SET_NULL,
        null=True,
    )
    car= models.ForeignKey(
        Car,
        on_delete=models.SET_NULL,
        null=True,
    )
    start_taxiing_time = models.DateTimeField(auto_now_add=True)
    stop_taxiing_time = models.DateTimeField()

    def __str__(self):
        return " "
