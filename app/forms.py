from django import forms
from .models import Produto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['imagem', 'nome', 'preco', 'estoque', 'desconto', 'apagado']


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limpa as listas gigantes de help_text do Django
        self.fields['username'].help_text = None
        self.fields['username'].label = "Usuário"
        
        self.fields['password1'].help_text = None
        self.fields['password1'].label = "Senha"
        
        self.fields['password2'].help_text = None
        self.fields['password2'].label = "Confirmar Senha"