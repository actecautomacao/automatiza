
class Produtos:

    def __init__(self, codigo_produto = 'Sem código'):
        self._codigo_produto = codigo_produto

    def regist_produc(self):
        registro1 = str(input('Informe codigo produto: '))
        self._codigo_produto = registro1
        print(f'O codigo do produto informado foi: {self._codigo_produto}')

    def getCodigoProduto(self):
        return self._codigo_produto








