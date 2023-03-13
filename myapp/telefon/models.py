from django.db import models

# Create your models here.
class Phones(models.Model):
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50, verbose_name='Модель')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена в $')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    color = models.CharField(max_length=20, default='black', verbose_name='Цвет')



    class Meta:
        db_table = 'Phone'
        verbose_name_plural = 'Телефоны'
        verbose_name = 'Телефон'
        ordering = ('price',)

    def __str__(self):
        return f'{self.title} - {self.price}'

class Brand(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name}'


# class Phones(models.Model):
#     brand = models.ForeignKey('PhoneModel', on_delete=models.CASCADE, verbose_name='Марка')
#     model = models.CharField(max_lenght=150, verbose_name='Модель')
#     content = models.TextField(null=True, blank=True, verbose_name='Описание')
#     price = models.IntegerField(null=True, verbose_name='Цена')
#     date = models.DateTimeField(auto_now_add=True, db_index=True)
#     vin = models.IntegerField(null=True, name='Number car: ', verbose_name='Вин номер')
#     color = models.CharField(max_lenght=50 , default='black', verbose_name='Цвет')