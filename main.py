# -*- coding: latin-1 -*-
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
    comprimento = float(input("Comprimento (18-23m): "))
    peso = float(input("Peso (100-200 tons): "))
    potencia = float(input("Potência (2000-6000 HP): "))
    return Locomotiva(comprimento, peso, potencia)

def obter_dados_passageiro():
    print("=== DADOS DO VAGAO DE PASSAGEIROS ===")
    comprimento = float(input("Comprimento (22-26m): "))
    peso = float(input("Peso (30-50 tons): "))
    passageiros = int(input("Número de passageiros (até 50): "))
    return Passageiro(comprimento, peso, passageiros)

def obter_dados_carga():
    print("=== DADOS DO VAGÃO DE CARGA ===")
    comprimento = float(input("Comprimento (12-19m): "))
    peso = float(input("Peso total (15-30 tons): "))
    carga = float(input("Carga transportada (75% do peso): "))
    return Carga(comprimento, peso, carga)

def inserir_vagao(composicao):
    print("\n=== INSERIR VAGAO ===")
    print("1. Locomotiva")
    print("2. Vagao de passageiros")
    print("3. Vagao de carga")

    tipo = input("Escolha o tipo (1-3): ")
    
    if tipo == "1":
        vagao = obter_dados_locomotiva()
    elif tipo == "2":
        vagao = obter_dados_passageiro()
    elif tipo == "3":
        vagao = obter_dados_carga()
    else:
        print("Tipo invalido!")
        return
    
    print("\nOnde inserir?")
    print("1. Na frente")
    print("2. No final")

    posicao = input("Escolha a posicao (1-2): ")

    try:
        if posicao == "1":
            composicao.inserir_vagao_frente(vagao)
            print("Vagao inserido na frente com sucesso!")
        elif posicao == "2":
            composicao.inserir_vagao_final(vagao)
            print("Vagao inserido no final com sucesso!")
        else:
            print("Posicao invalida!")
    except Exception as e:
        print(f"Erro ao inserir vagao: {e}")

def remover_vagao(composicao):
    print("\n=== REMOVER VAGAO ===")
    print("1. Do inicio")
    print("2. Do final")

    posicao = input("Escolha a posicao (1-2): ")

    try:
        if posicao == "1":
            vagao = composicao.remover_vagao_inicio()
            if vagao:
                print("Vagao removido do início com sucesso!")
            else:
                print("Composicao vazia!")
        elif posicao == "2":
            vagao = composicao.remover_vagao_final()
            if vagao:
                print("Vagao removido do final com sucesso!")
            else:
                print("Composicao vazia!")
        else:
            print("Posiçao invalida!")
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
        opcao = input("Escolha uma opcao (a-g): ").lower()
        
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
            
        else:
            print("Opcao invalida! Tente novamente.")

if __name__ == "__main__":
    main()