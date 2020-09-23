
from registrousuario import connect1


while True:
    operacao = int(input('Informe senha padrão (223) para processeguir: '))
    try:
        if operacao != 223:
            print('Usuario Invalido!')
        elif operacao == 223:
            print('Inicio do processo!! ')
            print(operacao)
            connect1(operacao)  # chamada da função dentro do arquivo registro de usuarios.py
    except ValueError:
        print('Erro de valor')



