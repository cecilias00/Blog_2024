# urls solo de la app posts
from django.urls import path
from . import views
from .views import contactanos_view 
from .views import nuevo_post
from .views import eliminar_post
from .views import agregar_comentario
from .views import eliminar_comentario  

urlpatterns = [
    path("", views.posts, name="noticias"),
    path("quienessomos/", views.about_us, name="quienessomos"),
    path("registro/", views.Registro.as_view(), name="registro"),
    path("postindividual/<int:id>/", views.post_id, name="postindividual"),
    path('post/<int:post_id>/comentario/', agregar_comentario, name='agregar_comentario'),
    path('contactanos/', contactanos_view, name='contactanos'),
    path('nuevo_post/', nuevo_post, name='nuevo_post'),
    path('posts/eliminar/<int:id>/', eliminar_post, name='eliminar_post'),
    path('comentarios/eliminar/<int:comentario_id>/', eliminar_comentario, name='eliminar_comentario'), 
]




        # crear nuevo post
    # path("nuevo_post/", views.CrearPost.as_view(), name="nuevo_post"),
    # # eliminar
    # path("eliminar/<int:pk>", views.EliminarPost.as_view(), name="eliminar_post"),
    # # modificar
    # path("modificar/<int:pk>", views.ModificarPost.as_view(), name="modificar_post"),
    # # perfil del usuario
    # path("perfil/<int:id>", views.perfil, name="perfil"),
    # # url de comentario
    # path("comentar/", views.comentar_post, name="comentar"),