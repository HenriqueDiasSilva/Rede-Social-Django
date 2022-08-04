from django.contrib import admin
from .models import Colaborador, Publicacao, Comentario, Seguir


@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    pass


@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    pass


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    pass


@admin.register(Seguir)
class SeguirAdmin(admin.ModelAdmin):
    pass
