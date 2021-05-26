from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, DetailView
from django.http import JsonResponse

from .models import Usuario

class UsuarioListaView(ListView):
	model = Usuario
	template_name = 'usuario/lista.html'

	def post(self, request, *args, **kwargs):
		data = {}
		try:
			action = request.POST['action']
			if action == 'searchdata':
				data = []
				for i in Usuario.objects.all():
					data.append(i.toJSON())
			else:
				data['Error'] = 'Ha ocurrido un error'

		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data, safe=False)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['titulo'] = 'Listado de Usuarios'
		context['craer_url'] = reverse_lazy()
		context['lista_url'] = reverse_lazy()
		context['entidad'] = 'Usuarios'
		return context