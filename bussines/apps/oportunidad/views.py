from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from apps.oportunidad.forms import OportunidadForm
from django.core import serializers
from apps.oportunidad.models import Oportunidad
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.

def listadousuarios(request):
	lista = serializers.serialize('json', User.objects.all(), fields=['username', 'first_name'])
	return HttpResponse(lista, content_type='application/json')

def index(request):
	return render(request, 'oportunidad/index.html')

def oportunidad_view(request):
	if request.method == 'POST':
		form = OportunidadForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('oportunidad:oportunidad_listar')
	else:
		form = OportunidadForm()
	return render(request, 'oportunidad/oportunidad_form.html', {'form':form})

def oportunidad_list(request):
	oportunidad = Oportunidad.objects.all()
	contexto = {'oportunidad':oportunidad, 'form':form}
	return render(request, 'oportunidad/oportunidad_list.html', contexto)

def oportunidad_edit(request, id_oportunidad):
	oportunidad = Oportunidad.objects.get(id=id_oportunidad)
	if request.method == 'GET':
		form = OportunidadForm(instance=oportunidad)
	else:
		form = OportunidadForm(request.POST, instance=oportunidad)
		if form.is_valid():
			form.save()
		return redirect('oportunidad:oportunidad_listar')
	return render(request, 'oportunidad/oportunidad_form.html', {'form':form})

def oportunidad_delete(request, id_oportunidad):
	oportunidad = Oportunidad.objects.get(id=id_oportunidad)
	if request.method == 'POST':
		oportunidad.delete()
		return redirect('oportunidad:oportunidad_listar')
	return render(request, 'oportunidad/oportunidad_delete.html', {'oportunidad':oportunidad})

class OportunidadList(ListView):
	model = Oportunidad
	template_name = 'oportunidad/oportunidad_list.html'
	paginate_by = 2

class OportunidadCreate(CreateView):
	model = Oportunidad
	form_class = OportunidadForm
	template_name = 'oportunidad/oportunidad_form.html'
	success_url = reverse_lazy('oportunidad:oportunidad_listar')

class OportunidadUpdate(UpdateView):
	model = Oportunidad
	form_class = OportunidadForm
	template_name = 'oportunidad/oportunidad_form.html'
	success_url = reverse_lazy('oportunidad:oportunidad_listar')

class OportunidadDelete(DeleteView):
	model = Oportunidad
	template_name = 'oportunidad/oportunidad_delete.html'
	success_url = reverse_lazy('oportunidad:oportunidad_listar')