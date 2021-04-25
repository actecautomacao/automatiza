from Modelos import equipamentos
from Modelos import produtos
from Modelos import usuario
from Modelos import recupera

import sys

sys.path.append("Modelos/usuario.py")
sys.path.append('Modelos/equipamentos.py')
sys.path.append('Modelos/produtos.py')

userman = usuario.Usuario()
userman.regist_user()

equip = equipamentos.Equipamentos()
equip.regist_equip()

produc = produtos.Produtos()
produc.regist_produc()

recp = recupera.Recupera(userman.getCodigoUsuario(),equip.getCodigoEquipamento(),produc.getCodigoProduto())
recp.imprimi()