from django.contrib import admin

from .models import categoria, producto, Cliente, Venta, detallesventas

admin.site.register(categoria)
admin.site.register(producto)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(detallesventas)