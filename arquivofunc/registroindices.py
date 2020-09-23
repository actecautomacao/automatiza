from registrocomponentes import connect4

indices = []
indicestemp = []


def connect3(registro_indices):

    while True:

        registroindice = str(input('Informe o indice de manutenção para proceguir:  '))
        if registroindice != '125':
            print('indice Invalida')
        else:
            indicestemp.append(registroindice[:])
            indices.append(indicestemp[:])
            indicestemp.clear()
            print(f'O indices registrado foi {indices[:]}')
            connect4(registro_indices)  # chamada da função dentro do arquivo registro de componentes
            # (registrocomponentes.py)
