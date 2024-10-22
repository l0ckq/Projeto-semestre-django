from django.db import models

class Categoria(models.Model): # Associa como uma tabela dentro do DB
    nome = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome
    
class Produto(models.Model):                
    nome = models.CharField(max_length = 100)
    preco = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE) # FK do ID da outro tabela: Categoria
    imagem = models.ImageField(upload_to = 'produtos/', null = True, blank = True)

    def __str__(self):
        return self.nome
    
