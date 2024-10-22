from django import forms
from projeto.models import Categoria, Produto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        labels = {
            'nome' : 'Nome da Categoria', 
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'categoria', 'imagem']
        labels = {
            'nome' : 'Nome do Produto', 
            'preco' : 'Preço (R$)',
            'categoria' : 'Categoria',
            'imagem' : 'Imagem do Produto'
        }

# Usamos esse forms para usar o modelo do próprio django e "ecnonomizar" HTML e fazer o django fazer por si só esse formulário.