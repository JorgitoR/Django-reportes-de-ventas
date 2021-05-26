from django.urls import path



from .views import (

	UsuarioListaView,
	UsuarioCrearView,
	UsuarioActualizar,
	UsuarioDeleteView, 
	UsuarioCambiarGrupo,
	UsuaioPerfil

	)

urlpatterns = [
	
	path('lista/', UsuarioListaView.as_view(), name='usuario_lista'),
	path('crear/', UsuarioCrearView.as_view(), name='usuario_crear'),
	path('actualizar/<int:pk>/', UsuarioActualizar.as_view(), name='usuario_actualizar'),
	path('eliminar/<int:pk>/', UsuarioDeleteView.as_view(), name='usuario_eliminar'),
	path('cambiar/grupo/<int:pk>/', UsuarioCambiarGrupo.as_view(), name='usuario_grupo'),
	path('perfil/', UsuaioPerfil.as_view(), name='usuario_perfil'),

]