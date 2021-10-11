from django.contrib import admin
from apps.business.views import index_business, BusinessList, BusinessCreate, BusinessUpdate, BusinessDelete
from django.urls import path, re_path, include

urlpatterns = [
    path('', index_business, name='inicio'),
    path('business/listar', BusinessList.as_view(), name='business_listar'),
    path('business/nueva', BusinessCreate.as_view(), name='business_crear'),
    path('business/editar/<pk>/', BusinessUpdate.as_view(), name='business_editar'),
    path('business/eliminar/<pk>/', BusinessDelete.as_view(), name='business_eliminar'),
]
