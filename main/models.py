from django.db import models


class Address(models.Model):
    name = models.CharField(max_length=100, unique=True)
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    class Meta:
        verbose_name = 'Адрес магазина'
        verbose_name_plural = 'Адреса магазинов'

    def __str__(self):
        return self.name
