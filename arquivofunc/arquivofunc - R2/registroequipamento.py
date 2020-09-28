from registroindices import connect3


def connect2(codigo_equipamento):

    codigoequipamento = str(input('Informe codigo do equipamento 2 digitos para proceguir:   '))
    while True:
        try:
            if len(codigoequipamento) != 2:
                print('Codido Invalido')
                break
            elif len(codigoequipamento) == 2:
                print('Equipamento registrado com sucesso')
                print(codigoequipamento)
                return connect3(codigo_equipamento, codigoequipamento)  # chamada da função dentro do arquivo registro de indices (registroindices.py)
        except ValueError:
            print('Valor invalido')

