from django.contrib import admin
from django.contrib.auth.decorators import login_required
from apps.oportunidad.views import listadousuarios, index, oportunidad_view, oportunidad_list, oportunidad_edit, oportunidad_delete, OportunidadList, OportunidadCreate, OportunidadUpdate, OportunidadDelete
from django.urls import path, re_path, include
app_name = 'oportunidad'
urlpatterns = [
    path('',index,name='index'),
    path('nuevo/',login_required(OportunidadCreate.as_view()),name='oportunidad_crear'),
    path('listar/',login_required(OportunidadList.as_view()),name='oportunidad_listar'),
    path('editar/<pk>/',login_required(OportunidadUpdate.as_view()),name='oportunidad_editar'),
    path('eliminar/<pk>/',login_required(OportunidadDelete.as_view()),name='oportunidad_eliminar'),
    path('listado/', listadousuarios,name='listado'),
]
