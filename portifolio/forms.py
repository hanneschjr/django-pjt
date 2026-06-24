from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class ContatoForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Digite seu nome",
                'class': 'modal-input'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': "Digite seu e-mail para contato",
                'class': 'modal-input'
            }
        )
    )
    assunto = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': "Digite assunto",
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
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox(
            attrs={
                'data-theme': 'dark',
            }
        )
    )