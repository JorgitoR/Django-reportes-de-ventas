from django import forms
from .Usuario import Usuario

class UsuarioForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs['autofocus'] = True

	class Meta:
		model = Usuario
		fields = [
			'first_name',
			'last_name',
			'email',
			'username',
			'password',
			'image',
			'groups'

		]

		widget = {

		
		}