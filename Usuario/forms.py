from django import forms
from .models import Usuario

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
			'imagen',
			'groups'

		]

		widget = {

			'first_name': forms.TextInput(
				attrs={
					'placeholder':'Ingrese su nombre',
				}
			),
			'last_name': forms.TextInput(
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
					'class': 'form-control select2',
					'style': ' width:100%',
					'multiple': 'multiple',
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
		data = {}
		form = super()
		try:
			if form.is_valid():
				password = self.cleaned_data['password']
				u = form.save(commit=False)
				if u.pk is None:
					u.set_password(password)
				else:
					usuario = Usuario.objects.get(pk=u.pk)
					if usuario.password != password:
						u.set_password(password)
				u.save()
				u.groups.clear()

				for g in self.cleaned_data['groups']:
					u.groups.add(g)

			else:
				data['errores'] = form.errors

		except Exception as e:
			data['error'] = str(e)

		return data