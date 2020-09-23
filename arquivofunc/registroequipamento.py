from registroindices import connect3


def connect2(codigo_equipamento):

    codigoequipamento = int(input('Informe codigo do equipamento 3 digitos para proceguir:   '))
    while True:
        try:
            if codigoequipamento != 124:
                print('Codido Invalido')
                break
            elif codigoequipamento == 124:
                print('Equipamento registrado com sucesso')
                print(codigoequipamento)
                connect3(codigo_equipamento)  # chamada da função dentro do arquivo registro de indices (registroindices.py)
        except ValueError:
            print('Valor invalido')

