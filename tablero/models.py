from django.db import models

from django.forms import model_to_dict

from AppVentas.settings import MEDIA_URL, STATIC_URL

class categoria(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

class producto(models.Model):
	categoria = models.ForeignKey(categoria)
	nombre = models.CharField(max_length=150, verbose_name='Nombre del producto')
	imagen = models.ImageField(upload_to='producto/%Y/%m/%d', null=True, blank=True)
	stock = models.IntegerField(default=0, verbose_name='Stock')
	pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='precio de venta')

	def __str__(self):
		return self.nombre

	def toJSON(self):
		item = model_to_dict(self)
		item['full_name'] = '{} / {}'.format(self.nombre, self.categoria.nombre)
		item['categoria'] = self.categoria.toJSON()
		item['imagen'] = self.get_imagen()
		item['pvp'] = format(self.pvp, '.2f')
		return item

	def get_imagen(self):
		if self.imagen:
			return '{}{}'.format(MEDIA_URL, self.imagen)
		return '{}{}'.format(STATIC_URL, 'img/empty.png')

	class Meta:
		verbose_name = 'Producto'
		verbose_name_plurarl = 'Productos'
		ordering = ['id']


