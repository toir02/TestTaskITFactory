from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    phone_number = models.CharField(max_length=255, verbose_name='Номер телефона')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class Store(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Сотрудник')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговые точки'


class Visit(models.Model):
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')
    latitude = models.FloatField(verbose_name='Ширина')
    longitude = models.FloatField(verbose_name='Долгота')

    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='Торговая точка')

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'
