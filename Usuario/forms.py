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

			'first_name': forms.TextInput(
				attrs={
					'placeholder':'Ingrese su nombre',
				}
			),
			'last_name' forms.TextInput(
				attrs={
					'placeholder':'Ingrese su apellido',
				}
			),

			'email': forms.TextInput(
				attrs={
					'placeholder':'Ingrese su Email'
				}
			),

			'username': forms.TextInput(
				attrs={
					'placeholder':'Ingrese su usurname'
				}
			),

			'password': forms.PasswordInput(render_value=True,

				attrs={
					'placeholder':'Ingrese su password'
				}
			),

			'groups': forms.SelectMultiple(
				attrs={
					'class': 'form-control select2'
					'style': ' width:100%',
					'multiple': 'multiple'
				}
			)

		}

		exclude = [
			'user_permissions',
			'last_login',
			'date_joined',
			'is_superuser',
			'is_active',
			'is_staff'

		]

	def save(self, commit=True):