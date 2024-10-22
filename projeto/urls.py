from django.urls import path

from projeto.views import CategoriaCreateView, CategoriaDeleteView, CategoriaListView, CategoriaUpdateView, ProdutoCreateView, ProdutoDeleteView, ProdutoListView, ProdutoUpdateView


urlpatterns = [
    path('categoria/', CategoriaListView.as_view(), name="categoria_list"),
    path('categoria/nova/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categoria/<int:pk>/editar/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categoria/<int:pk>/excluir', CategoriaDeleteView.as_view(), name='categoria_delete'),

    path('', ProdutoListView.as_view(), name='produto_list'),
    path('produto/novo/', ProdutoCreateView.as_view(), name='produto_create'),
    path('produto/<int:pk>/editar/', ProdutoUpdateView.as_view(), name='produto_update'),
    path('produto/<int:pk>/excluir/', ProdutoDeleteView.as_view(), name='produto_delete'),
]
