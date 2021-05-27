from django.urls import path

from .views import ReporteVentas

urlpatterns = [
	
	path('reporte_venta/', ReporteVentas.as_view(), name='reporte_venta')

]