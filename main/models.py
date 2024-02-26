from django.db import models


class City(models.Model):
    """ Класс модели городов """
    name = models.CharField(max_length=100, unique=True, verbose_name='Город')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


    def __str__(self):
        return self.name


class Address(models.Model):
    """ Класс модели адресов магазинов """
    name = models.CharField(max_length=100, unique=True, verbose_name='Адрес магазина')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)


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


class ContactModel(models.Model):
    """ Класс модели обратной связи """
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Обратную связь  '
        verbose_name_plural = 'Обратная связь'


    def __str__(self):
        return f'{self.name} - {self.email}'