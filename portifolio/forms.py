from django import forms

class ContatoForm(forms.Form):

    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'modal-input'
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'modal-input'
            }
        )
    )

    assunto = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'modal-input'
            }
        )
    )

    mensagem = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'modal-textarea'
            }
        )
    )