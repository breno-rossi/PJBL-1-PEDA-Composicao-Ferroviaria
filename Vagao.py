
class Vagao:
    def __init__(self, comprimento, peso):
        self.comprimento = comprimento
        self.peso = peso

    def imprime(self):
        print(f"Comprimento: {self.comprimento} m, Peso: {self.peso} toneladas", end='')

class Locomotiva(Vagao):
    def __init__(self, comprimento, peso, potencia):
        super().__init__(comprimento, peso)
        self.potencia = potencia
        
    def imprime(self):
        super().imprime()
        print(" (Locomotiva)")
        print(f"Potência: {self.potencia} HP")
   
class Carga(Vagao):
    def __init__(self, comprimento, peso, carga):
        super().__init__(comprimento, peso)
        self.carga = carga

    def imprime(self):
        super().imprime()
        print(" (Carga)")
        print(f"Carga: {self.carga} ton")

class Passageiro(Vagao):
    def __init__(self, comprimento, peso, passageiros):
        super().__init__(comprimento, peso)
        self.passageiros = passageiros
        
    def imprime(self):
        super().imprime()
        print(" (Passageiro)")
        print(f"Passageiros: {self.passageiros}")
