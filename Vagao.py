
class Vagao:
    def __init__(self, comprimento, peso):
        self._comprimento = comprimento
        self._peso = peso
        
    
    def imprime(self):
        return (f'Dados do Vagão - Comprimento: {self._comprimento}, Peso: {self._peso}')


class Locomotiva(Vagao):
    def  __init__(self, comprimento, peso,potencia):
        self._potencia = potencia
        super().__init__(comprimento, peso)

    def imprime(self):
        super().imprime()
        return (f'Dados da Locomotiva - Potência: {self._potencia}')
   
class Carga(Vagao):
    def  __init__(self, comprimento, peso,carga):
        self._carga= carga
        super().__init__(comprimento, peso)

    def imprime(self):
        super().imprime()
        return (f'Dados do Vagão de Carga - Carga: {self._carga}')

class Passageiro(Vagao):
    def  __init__(self, comprimento, peso, capacidade):
        self._capacidade = capacidade
        super().__init__(comprimento, peso)

    def imprime(self):
        super().imprime()
        return (f'Dados do Vagão de Passageiro - Capacidade: {self._capacidade}')
