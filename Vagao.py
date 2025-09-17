
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


if __name__ == "__main__":
    
    locomotiva = Locomotiva(20, 150, 2500) #comprimento, peso, potencia
    vagao_carga = Carga(17, 20, 15) #comprimento, peso, carga
    vagao_passageiro = Passageiro(24, 40, 30) #comprimento, peso, passageiros

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