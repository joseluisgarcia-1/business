from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from apps.business.models import Persona, Business
from django.contrib.auth.models import User
# Create your views here.
from apps.business.forms import PersonaForm, BusinessForm
from django.urls import reverse_lazy

def index_business(request):
    return HttpResponse("Soy la página business")

class BusinessList(ListView):
    model = Business
    template_name = 'business/business_list.html'

class BusinessCreate(CreateView):
    model = Business
    template_name = 'business/business_form.html'
    form_class = BusinessForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('business:business_listar')

    def get_context_data(self, **kwargs):
        context = super(BusinessCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            business = form.save(commit=False)
            business.persona = form2.save()
            business.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class BusinessUpdate(UpdateView):
    model = Business
    second_model = Persona
    template_name = 'business/business_form.html'
    form_class = BusinessForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('business:business_listar')

    def get_context_data(self, **kwargs):
        context = super(BusinessUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        business = self.model.objects.get(id=pk)
        persona = self.second_model.objects.get(id=business.persona_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=persona)
        context['id'] = pk
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_business = kwargs['pk']
        business = self.model.objects.get(id=id_business)
        persona = self.second_model.objects.get(id=business.persona_id)
        form = self.form_class(request.POST, instance=business)
        form2 = self.second_form_class(request.POST, instance=persona)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class BusinessDelete(DeleteView):
    model = Business
    template_name = 'business/business_delete.html'
    success_url = reverse_lazy('business:business_listar')

