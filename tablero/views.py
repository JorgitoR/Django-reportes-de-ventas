from django.shortcuts import render
from django.views.generic import TemplateView

from .models import producto, Cliente, Venta, detallesventas
from django.db.models import Sum
from django.db.models.function import Coalesce

from django.http import JsonResponse

from random import randint


class TableroView(TemplateView):

	def get(self, request, *args, **kwargs):
		request.user.get_group_session()
		return super().get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = {}
		
