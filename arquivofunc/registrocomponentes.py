from registroman import gravaman

componentes = []
componentestemp = []


def connect4(registro_componentes):

    while True:

        registcomponet = str(input('Informe o componente de manutenção para proceguir:  '))
        if registcomponet != '126':
            print('indice Invalida')
            break
        else:
            componentestemp.append(registcomponet[:])
            componentes.append(componentestemp[:])
            componentestemp.clear()
            print(f'O Componente registrado foi {componentes[:]}')
            gravaman(registro_componentes)

