from django.shortcuts import render, redirect

def inicio(request):

	if request.user.is_authenticated:
		if request.user.is_staff:
			return redirect('reporte_venta')

	return render(request, 'inicio.html')