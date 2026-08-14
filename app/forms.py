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

class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Nome',
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Seu nome'})
    )
    last_name = forms.CharField(
        label='Sobrenome',
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Seu sobrenome'})
    )
    username = forms.CharField(
        label='Nome de Usuário',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Seu nome de usuário'})
    )
    email = forms.EmailField(
        label='E-mail',
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'seu@email.com'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    def clean_email(self):
        """
        Valida se o e-mail informado já está em uso por OUTRO usuário.
        """
        email = self.cleaned_data.get('email')
        if email:
            # Busca outros usuários com o mesmo e-mail ignorando o próprio usuário logado
            if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('Este e-mail já está em uso por outra conta.')
        return email

    def clean_username(self):
        """
        Valida se o nome de usuário já está em uso por OUTRO usuário.
        """
        username = self.cleaned_data.get('username')
        if username:
            if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('Este nome de usuário já está em uso.')
        return username