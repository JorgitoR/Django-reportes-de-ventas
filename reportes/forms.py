from django.forms import *

class ReporteForm(Form):
	date_range = CharField(widget=TextInput(attrs={
		'class': 'form-control',
		'autocomplete':'off'
	}))