from Modelos.usuario import *
from Modelos.produtos import *
from Modelos.equipamentos import *

import sys

sys.path.append("usuario.py")
sys.path.append('equipamentos.py')
sys.path.append('produtos.py')


class Recupera(Usuario, Equipamentos, Produtos):

    def __init__(self, codigo_usuario, codigo_equipamento, codigo_produto):
        Usuario.__init__(self,codigo_usuario)
        Equipamentos.__init__(self,codigo_equipamento)
        Produtos.__init__(self,codigo_produto)

    def imprimi(self):
        print(f'O codigo final recuperado foi:  ({self._codigo_usuario}),'
              f'({self._codigo_equipamento}),'
              f'({self._codigo_produto})')