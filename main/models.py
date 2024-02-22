from django.db import models


class Address(models.Model):
    """ Класс модели адресов магазинов """
    name = models.CharField(max_length=100, unique=True, verbose_name='Адрес магазина')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    class Meta:
        verbose_name = 'Адрес магазина'
        verbose_name_plural = 'Адреса магазинов'

    def __str__(self):
        return self.name


class Social(models.Model):
    """ Класс модели соц. сетей страницы о нас """
    icon = models.FileField(upload_to="icons/")
    name = models.CharField(max_length=200)
    link = models.URLField()

    class Meta:
        verbose_name = 'Социальные сети'
        verbose_name_plural = 'Социальные сети'

    def __str__(self):
        return self.name
