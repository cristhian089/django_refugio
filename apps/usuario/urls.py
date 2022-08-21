
from django.urls import path
from django.conf.urls import url
from apps.usuario.views import RegistroUsuario


app_name = 'usuario'
urlpatterns = [
    path('registrar', RegistroUsuario.as_view(),name='registrar')
]