from django.shortcuts import render
from microblogging.models import Colaborador, Publicacao, Comentario, Seguir
from microblogging.forms import PublicacaoForm, ComentarioForm
from django.views.generic import TemplateView, FormView, View
from django.urls import reverse


class PublicacaoView(FormView):
    template_name = 'microblogging/publicacao.html'
    form_class = PublicacaoForm

    def get(self, request):
        colaborador = Colaborador.objects.get(usuario=self.request.user)
        return render(request, self.template_name, {'colaborador': colaborador, 'form': self.form_class})

    def form_valid(self, form):
        user = self.request.user
        if user.is_authenticated:
            dados = form.clean()
            colaborador = Colaborador.objects.get(usuario=user)
            publicacao = Publicacao(
                texto=dados['publicacao'], colaborador=colaborador)
            publicacao.save()
            return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')


class ComentarioView(FormView):
    template_name = 'microblogging/comentario.html'
    form_class = ComentarioForm

    def get(self, request, **kwargs):
        colaborador = Colaborador.objects.get(usuario=self.request.user)
        publicacao = Publicacao.objects.get(pk=kwargs['publicacao_id'])
        return render(request, self.template_name, {'colaborador': colaborador, 'publicacao': publicacao, 'form': self.form_class})

    def form_valid(self, form):
        user = self.request.user
        if user.is_authenticated:
            dados = form.clean()
            usuario = Colaborador.objects.get(usuario=user)
            publicacao = Publicacao.objects.get(pk=dados['publicacao_id_form'])
            comentario = Comentario(
                texto=dados['comentario'], colaborador=usuario, publicacao=publicacao)
            comentario.save()
            return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')


class PublicacaoComentariosView(TemplateView):
    template_name = 'microblogging/publicacao_comentarios.html'

    def get(self, request, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            colaborador = Colaborador.objects.get(usuario__username=user)
            publicacao = Publicacao.objects.get(pk=kwargs['publicacao_id'])
            comentarios = Comentario.objects.filter(
                publicacao=kwargs['publicacao_id']).order_by('-id')
            return render(request, 'microblogging/publicacao_comentarios.html', {'colaborador': colaborador, 'publicacao': publicacao, 'comentarios': comentarios})


class IndexView(TemplateView):
    template_name = 'microblogging/index.html'

    def get(self, request):
        user = self.request.user
        if user.is_authenticated:
            colaborador = Colaborador.objects.get(usuario__username=user)
            seguidos = Seguir.objects.filter(seguidor=colaborador)
            publicacoes_seguidos = []
            for seguido in seguidos:
                publicacoes_seguidos += Publicacao.objects.filter(
                    colaborador=seguido.seguido)[:30]
            return render(request, 'microblogging/index.html', {'publicacoes_seguidos': publicacoes_seguidos})


def perfil(request, nome):
    user = request.user
    if user.is_authenticated:
        colaborador = Colaborador.objects.get(usuario__username=nome)
        publicacoes = Publicacao.objects.filter(
            colaborador__usuario__username=nome).order_by('-id')
        relacao = Seguir.objects.filter(
            seguidor__usuario__username=user, seguido__usuario__username=nome)
        return render(request, 'microblogging/perfil.html', {'user': user, 'colaborador': colaborador, 'publicacoes': publicacoes, 'relacao':relacao})


def seguir(request, nome):
    user = request.user
    if user.is_authenticated:
        seguidor = Colaborador.objects.get(usuario__username=user)
        seguido = Colaborador.objects.get(usuario__username=nome)
        relacao = Seguir.objects.get_or_create(
            seguidor=seguidor, seguido=seguido)
        print(relacao)
        if not relacao[1]:
            relacao[0].delete()
        return perfil(request,nome)
