from django.db import models
from django.db import transaction


# Create your models here.
class Phones(models.Model):
    PINK = 'Pink'
    BLACK = 'Black'
    WHITE = 'White'
    COLOR_CHANGE = [
        (PINK, 'Pink'),
        (BLACK, 'Black'),
        (WHITE, 'White'),
    ]
    MOBILE = 'Phone'
    LAPTOP = 'Laptop'
    TABLET = 'Tablet'
    SELECT_TYPE = [
        (MOBILE, 'Телефон'),
        (LAPTOP, 'Ноутбук'),
        (TABLET, 'Планшет'),
    ]

    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, null=True, verbose_name='Фирма')
    #electronic = models.ForeignKey('Electronic', null=True, on_delete=models.PROTECT, verbose_name='Электроника')
    types = models.CharField(max_length=20, choices=SELECT_TYPE, default=MOBILE, verbose_name='Выберите тип')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')###########
    title = models.CharField(max_length=50, verbose_name='Модель')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена в $')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    #color = models.CharField(max_length=20, blank=True, verbose_name='Цвет')
    color = models.CharField(max_length=5, choices=COLOR_CHANGE, default=BLACK, verbose_name='Выберите цвет')



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

class Electronic(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Электроника')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        db_table = 'electronic'
        verbose_name_plural = 'Электроника'
        verbose_name = 'Электроника'

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