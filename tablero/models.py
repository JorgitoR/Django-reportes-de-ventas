from django.db import models

from django.forms import model_to_dict
from datetime import datetime

from AppVentas.settings import MEDIA_URL, STATIC_URL

from Usuario.models import Usuario

genero = (

	('hombre', 'Masculino'),
	('mujer', 'Femenino')

)


class categoria(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

class producto(models.Model):
	categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
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
		verbose_name_plural = 'Productos'
		ordering = ['id']


class Cliente(models.Model):
	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)
	identidad = models.CharField(max_length=20)
	fecha_born = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
	direcion = models.CharField(max_length=30)
	gener = models.CharField(max_length=10, choices=genero, default='', verbose_name='Sexo')


	def __str__(self):
		return self.get_full_name()

	def get_full_name(self):
		return '{} {} / {}'.format(self.nombre, self.apellido, self.identidad)

	def toJSON(self):
		item = model_to_dict(self)
		item['genero'] = {'id': self.genero, 'nombre': self.get_gender_display()}
		item['fecha_born'] = self.fecha_born.strftime('%Y-%m-%d')
		item['full_name'] = self.get_full_name()
		return item

	class Meta:
		verbose_name = 'Cliente'
		verbose_name_plural = 'Clientes'
		ordering = ['id']


class Venta(models.Model):
	cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	date_joined = models.DateField(default=datetime.now)
	subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
	iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
	total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
	
	def __str__(self):
		return self.cliente.username

	def toJSON(self):
		item = model_to_dict(self)
		item['cliente'] = self.cliente.toJSON()
		item['subtotal'] = format(self.subtotal, '.2f')
		item['iva'] = format(self.iva, '.2f')
		item['total'] = format(self.total, '.2f')
		item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
		item['det'] = [i.toJSON() for i in sel.detallesventas_set.all()]
		return item

class detallesventas(models.Model):
	venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
	producto = models.ForeignKey(producto, on_delete=models.CASCADE)
	precio =  models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
	cantidad = models.IntegerField(default=0)
	subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)


	def __str__(self):
		return self.producto.nombre

	def toJSON(self):
		item = model_to_dict(self, exclude=['venta'])
		item['producto'] = self.producto.toJSON()
		item['precio'] = format(self.precio, '.2f')
		item['subtotal'] = format(self.subtotal, '.2f')
		return item

