
from src.model.DAO.base_db import BaseDB

class Estoque(BaseDB):
    def __init__(self):
        super().__init__("estoque.json")

    def ler_estoque_todo(self):
        return self.readList()

    def add_novo_produto_estoque(self,data):
        self.salve(data)
        print("Add com sucesso o produto no estoque")

    def incrementar_produto_no_estoque(self,id_produto,quantidade:int):
        linha,produto=[(index,produto) for index, produto in enumerate(self.ler_estoque_todo()) if produto["id"]==id_produto][0]
        produto["quantidade"]+=quantidade
        novaLista=self.ler_estoque_todo()
        novaLista[linha]=produto

        self.salveList(novaLista)


    def decrementar_produto_no_estoque(self,id_produto,quantidade:int):
        linha,produto=[(index,produto) for index, produto in enumerate(self.ler_estoque_todo()) if produto["id"]==id_produto][0]
        produto["quantidade"]-=quantidade
        novaLista=self.ler_estoque_todo()
        novaLista[linha]=produto

        self.salveList(novaLista)

    def buscar_por_id_produto_estoque(self,id):
        try:
            produtoEncontrado = [produto for produto in self.ler_estoque_todo()
                                 if produto["id"] == id][0]
            return produtoEncontrado
        except IndexError as e:
            raise ValueError("Produto não existe no estoque: ", e)



if __name__ == '__main__':
    estoque=Estoque()
    estoque.incrementar_produto_no_estoque(2,15)

