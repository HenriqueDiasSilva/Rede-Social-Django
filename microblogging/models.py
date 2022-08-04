from django.db import models
from django.contrib.auth.models import User


class Colaborador (models.Model):
    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

    nome = models.CharField('Nome', max_length=128)
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    email = models.EmailField('E-mail')
    telefone = models.CharField(
        'Telefone', max_length=11, help_text='Apenas números')

    def __str__(self):
        return self.nome


class Publicacao (models.Model):
    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

    texto = models.TextField('Texto')
    colaborador = models.ForeignKey(
        Colaborador, on_delete=models.CASCADE, verbose_name='Colaborador')
    data_de_publicacao = models.DateField(
        'Data de publicação', auto_now_add=True)

    def __str__(self):
        return str(self.colaborador)


class Comentario(models.Model):

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    texto = models.TextField('Texto', max_length=200)
    colaborador = models.ForeignKey(
        Colaborador, on_delete=models.CASCADE, verbose_name='Colaborador')
    publicacao = models.ForeignKey(
        Publicacao, on_delete=models.CASCADE, verbose_name='Publicação')
    data_de_publicacao = models.DateField(
        'Data de publicação', auto_now_add=True)

    def __str__(self):
        return str(self.colaborador)


class Seguir(models.Model):

    class Meta:
        verbose_name = 'Seguir'
        verbose_name_plural = 'Seguir'

    seguidor = models.ForeignKey(
        Colaborador, on_delete=models.CASCADE, related_name='Seguidor')
    seguido = models.ForeignKey(
        Colaborador, on_delete=models.CASCADE, related_name='Seguido')
    data_que_seguiu = models.DateField(
        'Data que seguiu', auto_now_add=True)

    def __str__(self):
        return str(self.seguidor) + ' está seguindo ' + str(self.seguido)
