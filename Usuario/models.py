from django.db import models
from django.contrib.auth.models import AbstracUser

from django.forms import model_to_dict

from settings import MEDIA_URL, STATIC_URL

class Usuario(AbstracUser):
	imagen = models.ImageField(upload_to='usuario/%Y/%m/%d', null=True, blank=True)
	token = models.UUIDField(primary_key=False, editable=False, null=True, blank=True)

	def get_imagen(self):
		if self.imagen:
			return '{}{}'.format(MEDIA_URL, self.imagen)
		return '{}{}'.format(STATIC_URL, 'img/empty.png')

	def toJSON(self):
		item = model_to_dict(self, exclude=['password', 'user_permissions', 'last_login'])
		if self.last_login:
			item['last_login'] = self.last_login.strftime('%Y-%m-%d')
		item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
		item['image'] = self.get_imagen()
		item['full_name'] = self.get_full_name()
		item['groups'] = [{'id':g.id, 'name':g.name} for g in self.groups.all()]
		return item
		