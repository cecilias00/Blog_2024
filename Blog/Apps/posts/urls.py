# urls solo de la app posts
from django.urls import path
from . import views
from .views import contactanos_view  # Conserva solo esta línea
from .views import nuevo_post
from .views import eliminar_post

urlpatterns = [
    path("", views.posts, name="noticias"),  # Esto está bien
    path("quienessomos/", views.about_us, name="quienessomos"),
    path("registro/", views.Registro.as_view(), name="registro"),
    path("postindividual/<int:id>", views.post_id, name="postindividual"),
    path('contactanos/', contactanos_view, name='contactanos'),
    path('nuevo_post/', nuevo_post, name='nuevo_post'),
    path('posts/eliminar/<int:id>/', eliminar_post, name='eliminar_post'),
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