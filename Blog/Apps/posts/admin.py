from django.contrib import admin
from .models import Posts, Categorias, Comentarios

# Register your models here.
admin.site.register(Posts)
admin.site.register(Categorias)
admin.site.register(Comentarios)