
class Estoque:

    def __init__(self,id_produto:int,quantidade:int):
        self.__id_produto=id_produto
        self.__quantidade=quantidade

    @property
    def id_produto(self):
        return self.__id_produto

    @property
    def quantidade(self):
        return  self.__quantidade


    def addProdutos(self,quantidade:int):
        """
        Add produtos no estoque
        :param quantidade: int
        :return: None
        """
        self.__quantidade+=quantidade

    def removerProduto(self,quantidade:int):
        self.__quantidade-=quantidade

    def estoque(self):
        return{
            "id_produto":self.__id_produto,
            "quantidade":self.__quantidade
        }