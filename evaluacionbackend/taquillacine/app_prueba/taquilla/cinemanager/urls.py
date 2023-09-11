from django.urls import path
from . import views

app_name = 'cineapp' 

urlpatterns = [
    #URLs para peliculas
    path('', views.ListaPeliculasView.as_view(), name='lista_peliculas'),
    path('peliculas/<int:pk>/', views.DetallePeliculaView.as_view(), name='detalle_pelicula'),
    path('peliculas/crear/', views.CrearPeliculaView.as_view(), name='crear_pelicula'),
    path('peliculas/<int:pk>/actualizar/', views.ActualizarPeliculaView.as_view(), name='actualizar_pelicula'),
    path('peliculas/<int:pk>/eliminar/', views.EliminarPeliculaView.as_view(), name='eliminar_pelicula'),

    #URLs para horarios
    path('peliculas/<int:pelicula_id>/horarios/', views.ListaHorariosPeliculaView.as_view(), name='lista_horarios_pelicula'),
    path('pelicula/<int:pelicula_id>/agregar_horario/', views.agregar_horario, name='agregar_horario'),
    path('editar_horario/<int:horario_id>/', views.editar_horario, name='editar_horario'),
    path('eliminar_horario/<int:horario_id>/', views.eliminar_horario, name='eliminar_horario'),

    #URLs para asientos
    path('pelicula/<int:pelicula_id>/asientos/', views.AsientoList.as_view(), name='asiento_list'),
    path('pelicula/<int:pelicula_id>/asientos/create/', views.AsientoCreate.as_view(), name='asiento_create'),
    path('pelicula/<int:pelicula_id>/asientos/<int:asiento_id>/update/', views.AsientoUpdate.as_view(), name='asiento_update'),
    path('pelicula/<int:pelicula_id>/asientos/<int:pk>/delete/', views.AsientoDelete.as_view(), name='asiento_delete'),
]
