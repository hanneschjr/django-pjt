from django import forms

class ContatoForm(forms.Forms):
    name = forms.CharField()
    email = forms.EmailField()
    assunto = forms.CharField()
    mensagem = forms.CharField(widget=forms.Textarea)