from django import forms

class ContatoForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    assunto = forms.CharField()
    mensagem = forms.CharField(widget=forms.Textarea)