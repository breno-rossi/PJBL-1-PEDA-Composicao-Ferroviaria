# -*- coding: latin-1 -*-
from ComposicaoFerroviaria import ComposicaoFerroviaria
from Vagao import Locomotiva, Passageiro, Carga

def mostrar_menu():
    print("\n=== SISTEMA DE COMPOSI��O FERROVI�RIA ===")
    print("a. Criar composi��o padr�o")
    print("b. Inserir vag�o")
    print("c. Remover vag�o")
    print("d. Apresentar descri��o da composi��o")
    print("e. Apresentar dados do primeiro vag�o")
    print("f. Apresentar dados do �ltimo vag�o")
    print("g. Terminar")
    print("=" * 40)

def obter_dados_locomotiva():
    print("=== DADOS DA LOCOMOTIVA ===")
    comprimento = float(input("Comprimento (18-23m): "))
    peso = float(input("Peso (100-200 tons): "))
    potencia = float(input("Pot�ncia (2000-6000 HP): "))
    return Locomotiva(comprimento, peso, potencia)

def obter_dados_passageiro():
    print("=== DADOS DO VAG�O DE PASSAGEIROS ===")
    comprimento = float(input("Comprimento (22-26m): "))
    peso = float(input("Peso (30-50 tons): "))
    passageiros = int(input("N�mero de passageiros (at� 50): "))
    return Passageiro(comprimento, peso, passageiros)

def obter_dados_carga():
    print("=== DADOS DO VAG�O DE CARGA ===")
    comprimento = float(input("Comprimento (12-19m): "))
    peso = float(input("Peso total (15-30 tons): "))
    carga = float(input("Carga transportada (75% do peso): "))
    return Carga(comprimento, peso, carga)

def inserir_vagao(composicao):
    print("\n=== INSERIR VAG�O ===")
    print("1. Locomotiva")
    print("2. Vag�o de passageiros")
    print("3. Vag�o de carga")
    
    tipo = input("Escolha o tipo (1-3): ")
    
    if tipo == "1":
        vagao = obter_dados_locomotiva()
    elif tipo == "2":
        vagao = obter_dados_passageiro()
    elif tipo == "3":
        vagao = obter_dados_carga()
    else:
        print("Tipo inv�lido!")
        return
    
    print("\nOnde inserir?")
    print("1. Na frente")
    print("2. No final")
    
    posicao = input("Escolha a posi��o (1-2): ")
    
    try:
        if posicao == "1":
            composicao.inserir_vagao_frente(vagao)
            print("Vag�o inserido na frente com sucesso!")
        elif posicao == "2":
            composicao.inserir_vagao_final(vagao)
            print("Vag�o inserido no final com sucesso!")
        else:
            print("Posi��o inv�lida!")
    except Exception as e:
        print(f"Erro ao inserir vag�o: {e}")

def remover_vagao(composicao):
    print("\n=== REMOVER VAG�O ===")
    print("1. Do in�cio")
    print("2. Do final")
    
    posicao = input("Escolha a posi��o (1-2): ")
    
    try:
        if posicao == "1":
            vagao = composicao.remover_vagao_inicio()
            if vagao:
                print("Vag�o removido do in�cio com sucesso!")
            else:
                print("Composi��o vazia!")
        elif posicao == "2":
            vagao = composicao.remover_vagao_final()
            if vagao:
                print("Vag�o removido do final com sucesso!")
            else:
                print("Composi��o vazia!")
        else:
            print("Posi��o inv�lida!")
    except Exception as e:
        print(f"Erro ao remover vag�o: {e}")

def apresentar_dados_vagao(composicao, posicao):
    vagao = composicao.obter_dados_vagao(posicao)
    if vagao:
        print(f"\n=== DADOS DO {posicao.upper()} VAG�O ===")
        vagao.imprime()
    else:
        print(f"N�o h� vag�o na posi��o {posicao}!")

def main():
    # Cria uma composi��o ferrovi�ria com capacidade m�xima.
    composicao = ComposicaoFerroviaria(200, "composicao_ferroviaria.pkl")
    
    while True:
        mostrar_menu()
        opcao = input("Escolha uma op��o (a-g): ").lower()
        
        if opcao == "a":
            print("\n=== CRIANDO COMPOSI��O PADR�O ===")
            composicao.criar_composicao_padrao()
            print("Composi��o padr�o criada com sucesso!")
            
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
            print("Op��o inv�lida! Tente novamente.")

if __name__ == "__main__":
    main()