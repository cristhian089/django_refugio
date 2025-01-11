
from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.mascota.views import index, mascota_view,mascota_list, mascota_edit,mascota_delete,MascotaList,MascotaCreate,MascotaUpdate,MascotaDelete
app_name = 'mascota'
urlpatterns = [
    # path(r'^$', index),
    path('', index,name ='index'),
    #path('nuevo', mascota_view,name ='mascota_crear'), #url para la funcion de vista de crear
    path('nuevo', login_required(MascotaCreate.as_view()),name ='mascota_crear'),
    #path('listar', mascota_list,name ='mascota_listar'), #url para la funcion de vista
    path('listar', login_required(MascotaList.as_view()),name ='mascota_listar'),
    #path('editar/<id_mascota>/', mascota_edit,name ='mascota_editar'), #url para la funcion de vista editar
    path('editar/<pk>/', login_required(MascotaUpdate.as_view()),name ='mascota_editar'),
    #path('eliminar/<id_mascota>/', mascota_delete,name ='mascota_eliminar'), #urlpara las funcion eliminar
    path('eliminar/<pk>/', login_required(MascotaDelete.as_view()),name ='mascota_eliminar'),
]
