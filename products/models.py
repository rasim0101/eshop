from django.db import models

#функция для указания подпапок для фото товара
def product_photo_dir(instance, filename):
	# MEDIA_ROOT/
	# product_photos/_ID_/_FILENAME
	return 'product_photos/'+instance.id + '/' + filename

class Product(models.Model):
	"""Модель товаров в магазине"""
	SPORT = 'sport'
	SHOES = 'shoes'
	PHONE = 'phone'
	CATEGORIES = (
		# первое значение хранится в БД
		# второе видно зрителю
		('SPORT', 'Спортивные товары'),
		('SHOES', 'Обувь'),
		('PHONE', 'Мобильные телефоны'),
	)
	name = models.CharField(max_length=100, verbose_name="Название")
	description = models.TextField(verbose_name="Описание")
	created = models.DateTimeField(auto_now_add=True)#для автоматического значения при создании
	updated = models.DateTimeField(auto_now=True)#для автоматического изменения значения при обновлении записи
	price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена")#для деситичных дробей, пример: 125,50
	count = models.IntegerField(verbose_name="Количество", default=0)
	featured_product = models.BooleanField(default=False, verbose_name="Продвигать товар")
	category = models.CharField(max_length=5, choices=CATEGORIES, default=PHONE, verbose_name="Категория")
	photo = models.ImageField(upload_to='product_photos', default='default.jpg')

	def __str__(self):
		return f"{self.name} - {self.category}"


	class Meta:
		verbose_name="Товар"
		verbose_name_plural="Товары" 