# -*- coding: latin-1 -*-

# Disciplina: PEDA
# Professor: Dalton Vinicius Kozak
# Aluno: Francisco Bley Ruthes

from ComposicaoFerroviaria import ComposicaoFerroviaria
from Vagao import Locomotiva, Passageiro, Carga

def mostrar_menu():
    print("\n=== SISTEMA DE COMPOSICAO FERROVIARIA ===")
    print("a. Criar composicao padrao")
    print("b. Inserir vagao")
    print("c. Remover vagao")
    print("d. Apresentar descricao da composicao")
    print("e. Apresentar dados do primeiro vagao")
    print("f. Apresentar dados do ultimo vagao")
    print("g. Terminar")
    print("=" * 40)

def obter_dados_locomotiva():
    print("=== DADOS DA LOCOMOTIVA ===")
    
    while True:
        try:
            comprimento = float(input("Comprimento (18-23m): "))
            if 18 <= comprimento <= 23:
                break
            else:
                print("Erro: Comprimento deve estar entre 18m e 23m!")
        except ValueError:
            print("Erro: Digite um numero valido para o comprimento!")
    
    while True:
        try:
            peso = float(input("Peso (100-200 tons): "))
            if 100 <= peso <= 200:
                break
            else:
                print("Erro: Peso deve estar entre 100 e 200 toneladas!")
        except ValueError:
            print("Erro: Digite um numero valido para o peso!")
    
    while True:
        try:
            potencia = float(input("Potencia (2000-6000 HP): "))
            if 2000 <= potencia <= 6000:
                break
            else:
                print("Erro: Potencia deve estar entre 2000 HP e 6000 HP!")
        except ValueError:
            print("Erro: Digite um numero valido para a potencia!")
    
    return Locomotiva(comprimento, peso, potencia)

def obter_dados_passageiro():
    print("=== DADOS DO VAGAO DE PASSAGEIROS ===")
    
    while True:
        try:
            comprimento = float(input("Comprimento (22-26m): "))
            if 22 <= comprimento <= 26:
                break
            else:
                print("Erro: Comprimento deve estar entre 22m e 26m!")
        except ValueError:
            print("Erro: Digite um numero valido para o comprimento!")
    
    while True:
        try:
            peso = float(input("Peso (30-50 tons): "))
            if 30 <= peso <= 50:
                break
            else:
                print("Erro: Peso deve estar entre 30 e 50 toneladas!")
        except ValueError:
            print("Erro: Digite um numero valido para o peso!")
    
    while True:
        try:
            passageiros = int(input("Numero de passageiros (ate 50): "))
            if 1 <= passageiros <= 50:
                break
            else:
                print("Erro: Numero de passageiros deve estar entre 1 e 50!")
        except ValueError:
            print("Erro: Digite um numero inteiro valido para passageiros!")
    
    return Passageiro(comprimento, peso, passageiros)

def obter_dados_carga():
    print("=== DADOS DO VAGAO DE CARGA ===")
    
    while True:
        try:
            comprimento = float(input("Comprimento (12-19m): "))
            if 12 <= comprimento <= 19:
                break
            else:
                print("Erro: Comprimento deve estar entre 12m e 19m!")
        except ValueError:
            print("Erro: Digite um numero valido para o comprimento!")
    
    while True:
        try:
            peso = float(input("Peso total (15-30 tons): "))
            if 15 <= peso <= 30:
                break
            else:
                print("Erro: Peso deve estar entre 15 e 30 toneladas!")
        except ValueError:
            print("Erro: Digite um numero valido para o peso!")
    
    carga = 0.75 * peso  # 75% do peso total e considerado carga
    return Carga(comprimento, peso, carga)

def inserir_vagao(composicao):
    print("\n=== INSERIR VAGAO ===")
    print("1. Locomotiva")
    print("2. Vagao de passageiros")
    print("3. Vagao de carga")

    while True:
        tipo = input("Escolha o tipo (1-3): ")
        if tipo in ["1", "2", "3"]:
            break
        else:
            print("Erro: Tipo deve ser 1, 2 ou 3!")
    
    if tipo == "1":
        vagao = obter_dados_locomotiva()
    elif tipo == "2":
        vagao = obter_dados_passageiro()
    elif tipo == "3":
        vagao = obter_dados_carga()
    
    print("\nOnde inserir?")
    print("1. Na frente")
    print("2. No final")

    while True:
        posicao = input("Escolha a posicao (1-2): ")
        if posicao in ["1", "2"]:
            break
        else:
            print("Erro: Posicao deve ser 1 ou 2!")

    try:
        if posicao == "1":
            composicao.inserir_vagao_frente(vagao)
            print("Vagao inserido na frente com sucesso!")
        elif posicao == "2":
            composicao.inserir_vagao_final(vagao)
            print("Vagao inserido no final com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir vagao: {e}")

def remover_vagao(composicao):
    print("\n=== REMOVER VAGAO ===")
    print("1. Do inicio")
    print("2. Do final")

    while True:
        posicao = input("Escolha a posicao (1-2): ")
        if posicao in ["1", "2"]:
            break
        else:
            print("Erro: Posicao deve ser 1 ou 2!")

    try:
        if posicao == "1":
            vagao = composicao.remover_vagao_inicio()
            if vagao:
                print("Vagao removido do inicio com sucesso!")
            else:
                print("Composicao vazia!")
        elif posicao == "2":
            vagao = composicao.remover_vagao_final()
            if vagao:
                print("Vagao removido do final com sucesso!")
            else:
                print("Composicao vazia!")
    except Exception as e:
        print(f"Erro ao remover vagao: {e}")

def apresentar_dados_vagao(composicao, posicao):
    vagao = composicao.obter_dados_vagao(posicao)
    if vagao:
        print(f"\n=== DADOS DO {posicao.upper()} VAGAO ===")
        vagao.imprime()
    else:
        print(f"Nao ha vagao na posicao {posicao}!")

 #==============Programa principal=======================================
def main():
    
    composicao = ComposicaoFerroviaria(200, "composicao_ferroviaria.pkl")
    
    while True:
        mostrar_menu()
        
        while True:
            opcao = input("Escolha uma opcao (a-g): ").lower()
            if opcao in ["a", "b", "c", "d", "e", "f", "g"]:
                break
            else:
                print("Erro: Opcao deve ser uma letra de 'a' a 'g'!")
        
        if opcao == "a":
            print("\n=== CRIANDO COMPOSICAO PADRAO ===")
            composicao.criar_composicao_padrao()
            print("Composicao padrao criada com sucesso!")
            
        elif opcao == "b":
            inserir_vagao(composicao)
            
        elif opcao == "c":
            remover_vagao(composicao)
            
        elif opcao == "d":
            print("\n")
            composicao.diagnostico_composicao()
            
        elif opcao == "e":
            apresentar_dados_vagao(composicao, "primeiro")
            
        elif opcao == "f":
            apresentar_dados_vagao(composicao, "ultimo")
            
        elif opcao == "g":
            print("Encerrando o programa...")
            break

if __name__ == "__main__":
    main()