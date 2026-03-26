from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from registros import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_registros.registros, name="Principal"),
    path('contacto/', views_registros.contacto, name="Contacto"),
    path('nombre/', views.nombre, name="Nombre"),
    path('formulario/', views.formulario, name="Formulario"),
    path('ejemplo/', views.ejemplo, name="Ejemplo"),
    path('registrar/', views_registros.registrar, name="Registrar"),
    path('eliminarComentario/<int:id>/', views_registros.eliminarComentarioContacto, name="Eliminar"),
    path('editarComentario/<int:id>/', views_registros.editarComentarioContacto, name="Editar"),
    path('comentario/<int:id>/', views_registros.consultarComentarioIndividual, name="ConsultaIndividual"),
    path('consultar/', views_registros.consulta, name="Consulta"),
    path('consultas/', views_registros.consultar1, name="Consultas"),
    path('consultas2/', views_registros.consultar2, name="Consultas2"),
    path('consultas3/', views_registros.consultar3, name="Consultas3"),
    path('consultas4/', views_registros.consultar4, name="Consultas4"),
    path('consultas5/', views_registros.consultar5, name="Consultas5"),
    path('consultas6/', views_registros.consultar6, name="Consultas6"),
    path('consultas7/', views_registros.consultar7, name="Consultas7"),
    path('subir/', views_registros.archivos, name="Subir"),
    path('archivo/', views_registros.archivos, name="Archivos"),
    path('consultasSQL/', views_registros.consultasSQL, name="sql"),
    path('seguridad/', views.seguridad, name="seguridad"),
]

if settings.DEBUG:
    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


