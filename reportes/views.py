from django.shortcuts import render

from tablero.models import producto, Cliente, Venta, detallesventas
from .forms import ReporteForm

from django.db.models.functions import Coalesce
from django.db.models import Sum
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

class ReporteVentas(TemplateView):
	template_name = 'venta/reporte.html'

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):

		try:
			action = request.POST['action']
			if action == 'buscar_reporte':
				data = []
				fecha_inicio = request.POST.get('fecha_inicio', '')
				fecha_final = request.POST.get('fecha_final', '') 
				buscar = Venta.objects.all()
				if len(fecha_inicio) and len(fecha_final):
					buscar = buscar.filter(date_joined__range=[fecha_inicio, fecha_final])

				for s in buscar:
					data.append([

						s.id,
						s.cliente.nombre,
						s.date_joined.strftime('%Y-%m-%d'),
						format(s.subtotal, '.2f'),
						format(s.iva, '.2f'),
						format(s.total, '.2f')

					])

				subtotal = buscar.aggregate(r=Coalesce(Sum('subtotal'), 0)).get('r')
				print(subtotal)
				iva = buscar.aggregate(r=Coalesce(Sum('iva'), 0)).get('r')
				total = buscar.aggregate(r=Coalesce(Sum('total'), 0)).get('r')

				data.append([
					'----',
					'----',
					'----',
					format(s.subtotal, '.2f'),
					format(s.iva, '.2f'),
					format(s.total, '.2f')
				])
			else:
				data['error']='Ha ocurrido un error'

		except:
			pass
			
		return JsonResponse(data, safe=False)
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['titulo'] = 'Reportes de Ventas'
		context['entidad'] ='Reportes'
		context['lista_url'] = reverse_lazy('reporte_venta')
		context['form'] = ReporteForm()
		return context