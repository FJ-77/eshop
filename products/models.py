from django.db import models

class Product(models.Model):
	SPORT = 'SPORT'
	SHOES = 'SHOES'
	PHONE = 'PHONE'
	#Первое значение хранится в БД
	CATEGORIES = (
		(SPORT,'Спортивные товары'),
		(SHOES,'Обувь'),
		(PHONE,'Мобильные телефоны'),	
	)
	name = models.CharField(max_length=100, verbose_name='Название товара')
	description = models.TextField(verbose_name='Описание товара')
	created = models.DateTimeField(auto_now_add=True)#Создаётся один раз
	updated = models.DateTimeField(auto_now=True)#Будет менятся по мере обновления
	price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена товара')#Для десятичных дробей
	in_store = models.IntegerField(verbose_name='Кол-во в наличии')
	featured_product = models.BooleanField(default=False, verbose_name='Продвигаемый товар')
	category = models.CharField(max_length=5, choices=CATEGORIES, default=PHONE, verbose_name='Категория товара')

	def __str__(self):
		return f"{self.name} - {self.category}"

	class Meta:
		verbose_name='Товар'
		verbose_name_plural='Товары'	