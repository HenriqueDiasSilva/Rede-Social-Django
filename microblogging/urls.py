from django.urls import path
from microblogging.views import PublicacaoView, IndexView, PublicacaoComentariosView, ComentarioView, perfil, seguir


urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('publicacao/', PublicacaoView.as_view(), name='publicacao'),
    path('comentario/<int:publicacao_id>/',
         ComentarioView.as_view(), name='comentario'),
    path('comentarios/<int:publicacao_id>/',
         PublicacaoComentariosView.as_view(), name="comentarios"),
    path('<str:nome>/', perfil, name="perfil"),
    path('seguir/<str:nome>/', seguir, name="seguir"),

]
