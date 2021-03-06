from django.urls import path



from .views import (

	UsuarioListaView,
	UsuarioCrearView,
	UsuarioActualizar,
	UsuarioDeleteView, 
	UsuarioCambiarGrupo,
	UsuaioPerfil,

	UsuarioLogin,
	LogoutView,
	MisCompras

	)

urlpatterns = [
	
	path('login/', UsuarioLogin, name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('mis_compras/', MisCompras.as_view(), name='MisCompras'),
	path('lista/', UsuarioListaView.as_view(), name='usuario_lista'),
	path('crear/', UsuarioCrearView.as_view(), name='usuario_crear'),
	path('actualizar/<int:pk>/', UsuarioActualizar.as_view(), name='usuario_actualizar'),
	path('eliminar/<int:pk>/', UsuarioDeleteView.as_view(), name='usuario_eliminar'),
	path('cambiar/grupo/<int:pk>/', UsuarioCambiarGrupo.as_view(), name='usuario_grupo'),
	path('perfil/', UsuaioPerfil.as_view(), name='usuario_perfil'),

]