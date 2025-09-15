
class Vagao:
    def __init__(self, comprimento, peso):
        self._comprimento = comprimento
        self._peso = peso

    def imprime(self):
        print(f'--------------Dados do Vagão--------------------')
        print (f'Comprimento: {self._comprimento}m')
        print (f'Peso: {self._peso}Tons')

class Locomotiva(Vagao):
    def  __init__(self, comprimento, peso, potencia):
        super().__init__(comprimento, peso)
        self._potencia = potencia
        
    def imprime(self):
        super().imprime()
        print(f'Potência: {self._potencia}HP')
   
class Carga(Vagao):
    def  __init__(self, comprimento, peso,carga):
        super().__init__(comprimento, peso)
        self._carga= carga

    def imprime(self):
        super().imprime()
        print(f'Carga: {self._carga}ton')

class Passageiro(Vagao):
    def  __init__(self, comprimento, peso, capacidade):
        super().__init__(comprimento, peso)
        self._capacidade = capacidade
        
    def imprime(self):
        super().imprime()
        print(f'Capacidade: {self._capacidade} ')
        #print(f'Dados do Vagão de Passageiro - Capacidade: {self._capacidade}')


if __name__ == "__main__":
    
    locomotiva = Locomotiva(15, 5000, 3000) #comprimento, peso, potencia
    vagao_carga = Carga(12, 3000, 10000) #comprimento, peso,carga
    vagao_passageiro = Passageiro(14, 2500, 50) #comprimento, peso, capacidade

    print("=== Teste dos métodos imprime() ===\n")
    
    print("Locomotiva:")
    locomotiva.imprime()
    print()
    
    print("Vagão de Carga:")
    vagao_carga.imprime()
    print()
    
    print("Vagão de Passageiro:")
    vagao_passageiro.imprime()
    print()