from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView, View
from django.http import JsonResponse, HttpResponseRedirect

from .models import Usuario
from .forms import UsuarioForm

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

class UsuarioCrearView(CreateView):
	model = Usuario
	form_class = UsuarioForm
	template_name = 'usuario/crear.html'
	success_url = reverse_lazy()

	def post(self, request, *args, **kwargs):
		data = {}
		try:
			action = request.POST['action']

			if action == 'add':
				form = self.get_form()
				data = form.save()
			else:
				data['error']="No has ingresado alguna opcion"
		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['titulo'] = 'Creacion de usuarios'
		context['entidad'] ='Usuarios'
		context['lista_url'] = self.success_url
		context['action'] = 'add'
		return context


class UsuarioActualizar(UpdateView):
	model = Usuario
	form_class = UsuarioForm
	template_name = 'usuario/crear.html'
	success_url = reverse_lazy()

	def post(self, request, *args, **kwargs):
		data = {}

		try:
			action = request.POST['action']

			if action == 'edit':
				form = self.get_form()
				data = form.save()
			else:
				data['error'] = 'No has ingresado alguna opcion'

		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['titulo'] = 'Edicion de usuarios'
		context['entidad'] = 'Usuarios'
		context['lista_url'] = self.success_url
		context['action'] = 'edit'
		return context

class UsuarioDeleteView(DeleteView):
	model = Usuario
	template_name = 'usuario/eliminar.html'
	success_url = reverse_lazy()


	def post(self, request, *args, **kwargs):
		data = {}

		try: 
			self.object.delete()
		except Exception as e:
			data['error']= str(e)
		return JsonResponse(data)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['titulo']='Eliminacion de usuario'
		context['entidad'] = 'Usuarios'
		context['lista_url']=self.success_url
		return context

class UsuarioCambiarGrupo(View):

	def get(self, request, *args, **kwargs):
		try:
			request.session['group'] = Group.objects.get(pk=self.kwargs['pk'])
		except:
			pass
		return HttpResponseRedirect(reverse_lazy())