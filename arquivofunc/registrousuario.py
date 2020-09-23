
from registroequipamento import connect2


def connect1(registro_usuario):

    while True:
        usuario = int(input('Informe usuario para processeguir: '))
        try:
            if usuario != 321:
                print('Usuario Invalido!')
            elif usuario == 321:
                print('Usuario registrado com sucesso')
                print(usuario)
                connect2(registro_usuario)  # chamada da função dentro do arquivo registro de equipamentos registroequipamentos.py
        except ValueError:
            print('Erro de valor')