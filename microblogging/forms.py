from logging import PlaceHolder
from django import forms


class PublicacaoForm(forms.Form):

    publicacao = forms.CharField(label='', widget=forms.Textarea(
        attrs={'placeholder': 'O que você está pensando?', 'cols': 165, 'rows': 4}))

    def clean(self):
        dados = super().clean()
        publicacao = dados.get('publicacao')
        if len(publicacao) > 200:
            self.add_error('publicacao', 'Publicação de até 200 caracteres!!!')
        return dados


class ComentarioForm(forms.Form):

    publicacao_id_form = forms.IntegerField(widget=forms.HiddenInput())
    comentario = forms.CharField(label='', widget=forms.Textarea(
        attrs={'placeholder': 'O que você deseja comentar?', 'cols': 165, 'rows': 4}))
