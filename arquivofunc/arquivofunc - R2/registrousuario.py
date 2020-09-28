
from registroequipamento import connect2


def connect1(registro_usuario):

    while True:
        usuario = str(input('Informe usuario com 3 digitos para inicio do processo: '))
        try:
            if len(usuario) != 3:
                print('Usuario Invalido!')
            elif len(usuario) == 3:
                print('Usuario registrado com sucesso')
                print(usuario)
                return connect2(usuario)  # chamada da função dentro do arquivo registro de equipamentos registroequipamentos.py
        except ValueError:
            print('Erro de valor')