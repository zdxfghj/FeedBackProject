from django.db import models


class CarModel(models.Model):
    car_model = models.CharField(max_length=100, verbose_name="Car model")

    def __str__(self):
        return self.car_model

    class Meta:
        ordering = ('id',)
        verbose_name = 'Модель машины'
        verbose_name_plural = 'Модели машин'


class FeedBack(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name="Машина")
    year = models.IntegerField(verbose_name="Год выпуска машины")
    contact_info = models.TextField(verbose_name="Контактные данные для связи")
    email = models.EmailField(verbose_name="E-mail")
    damage_description = models.TextField(verbose_name="Описание повреждения", blank=True, null=True)

    def __str__(self):
        return str(self.car) + ' ' + str(self.year) + ' ' + self.damage_description

    class Meta:
        ordering = ('id',)
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'
