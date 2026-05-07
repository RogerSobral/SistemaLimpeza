from src.views.produto_view import ProdutoView
from src.controllers.produto_controller import ProdutoController
def  produtoConstructor(page):
    viewProduto=ProdutoView() # ela so pega dados do usuario
    produtoController=ProdutoController(page,viewProduto)


    return viewProduto
