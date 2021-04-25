
class Equipamentos:

    def __init__(self, codigo_equipamento='Sem código'):
        self._codigo_equipamento = codigo_equipamento

    def regist_equip(self):
        self._codigo_equipamento = input('Informe codigo Equipamento: ')
        print(f'O codigo equipamento informado foi: {self._codigo_equipamento}')

    def getCodigoEquipamento(self):
        return self._codigo_equipamento
