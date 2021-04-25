
class Usuario:

    def __init__(self, codigo_usuario='Sem código'):
        self._codigo_usuario = codigo_usuario

    def regist_user(self):
        self._codigo_usuario = input('Informe codigo usuario: ')
        print(f'O codigo usuario informado foi: {self._codigo_usuario}')

    def getCodigoUsuario(self):
        return self._codigo_usuario


