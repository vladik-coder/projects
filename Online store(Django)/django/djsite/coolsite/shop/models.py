from django.db import models
from django.urls import reverse


class Kazan(models.Model):
    price_new = models.IntegerField(verbose_name='Новая цена')
    price = models.IntegerField(verbose_name='Цена')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    volume = models.IntegerField(verbose_name='Объём')
    portions = models.IntegerField('Порции')
    wall_thickness = models.IntegerField('Толщина стенки')
    weight = models.IntegerField('Масса')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    class Meta:
        verbose_name = 'Казаны'
        verbose_name_plural = 'Казаны'
        ordering = ['id']

    def __int__(self):
        return self.volume

    def get_absolute_url(self):
        return reverse('about', kwargs={'post_id': self.pk})



