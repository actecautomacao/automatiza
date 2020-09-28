from registroman import gravaman

indices = []
indicestemp = []


def connect3(registro_indices):

    while True:

        registroindice = str(input('Informe o indice de manutenção com 4 digitos para proceguir:  '))
        if len(registroindice) != 4:
            print('indice Invalida')
        else:
            indicestemp.append(registroindice[:])
            indices.append(indicestemp[:])
            indicestemp.clear()
            print(f'O indices registrado foi {indices}')
            return gravaman(registro_indices, indices)  # chamada da função dentro do arquivo registro de componentes
            # (registrocomponentes.py)
