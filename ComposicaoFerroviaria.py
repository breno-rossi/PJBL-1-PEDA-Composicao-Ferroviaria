from DequeVC import Deque
from Persistencia import Persistente
from Vagao import Vagao, Locomotiva, Passageiro, Carga


class ComposicaoFerroviaria(Deque, Persistente):

    def __init__(self, N, nome_arquivo):
        # Inicializa o deque e o mecanismo de persistência.
        Deque.__init__(self, N)
        Persistente.__init__(self, nome_arquivo)
        self.carregar() # Carrega dados do arquivo, se existir.

    def salvar(self):
        # Salva a composição inteira no arquivo usando método herdado.
        Persistente.salvar(self, self)

    def carregar(self):
        # Carrega a composição do arquivo, se disponível.
        dados = Persistente.carregar(self)
        # Atualização dos dados da composição na memória (em uso).
        # O tamanho do vetor (_N) é assumido o mesmo.
        # Atualiza se dados não for None (arquivo não encontrado).
        if isinstance(dados, ComposicaoFerroviaria):
            self._data = dados._data
            self._size = dados._size
            self._front = dados._front
            self._top = dados._top

    def criar_composicao_padrao(self):
        # Apaga composição anterior: reinicializa a Composição Ferroviária (Deque).
        self._data = [None] * self._N
        self._size = 0
        self._front = 0
        self._top = 0
        
        # Cria a composição padrão conforme especificação do anexo.
        # 1 Locomotiva: 20m, 150 tons, 2500 HP
        locomotiva = Locomotiva(20, 150, 2500)
        self.addLast(locomotiva)
        
        # 50 Vagões de passageiros: 24m, 40 tons, 30 passageiros cada
        for i in range(50):
            vagao_passageiro = Passageiro(24, 40, 30)
            self.addLast(vagao_passageiro)
        
        # 30 Vagões de carga: 17m, 20 tons, 15 tons de carga cada
        for i in range(30):
            vagao_carga = Carga(17, 20, 15)
            self.addLast(vagao_carga)
        
        self.salvar()

    def inserir_vagao_frente(self, vagao):
        # Insere vagão na frente e salva automaticamente.
        self.addFirst(vagao)
        self.salvar()

    def inserir_vagao_final(self, vagao):
        # Insere vagão no final e salva automaticamente.
        self.addLast(vagao)
        self.salvar()

    def remover_vagao_inicio(self):
        # Remove vagão do início e salva automaticamente.
        if not self.isEmpty():
            vagao = self.deleteFirst()
            self.salvar()
            return vagao
        return None

    def remover_vagao_final(self):
        # Remove vagão do final e salva automaticamente.
        if not self.isEmpty():
            vagao = self.deleteLast()
            self.salvar()
            return vagao
        return None

    def contar_vagoes(self):
        # Retorna o número total de vagões e a quantidade de cada tipo.
        total_vagoes = self.getSize()
        locomotivas = 0
        passageiros = 0
        cargas = 0
        
        # Percorre todos os vagões para contar por tipo.
        for vagao in self._data:
            if vagao is not None:
                if isinstance(vagao, Locomotiva):
                    locomotivas += 1
                elif isinstance(vagao, Passageiro):
                    passageiros += 1
                elif isinstance(vagao, Carga):
                    cargas += 1
        
        return total_vagoes, locomotivas, passageiros, cargas

    def calcular_comprimento_total(self):
        # Calcula comprimento total considerando 2m entre vagões.
        if self.isEmpty():
            return 0
        
        comprimento_total = 0
        for vagao in self._data:
            if vagao is not None:
                comprimento_total += vagao.comprimento
        
        # Adiciona 2m entre cada vagão (número de vagões - 1 espaços).
        espacos_entre_vagoes = (self.getSize() - 1) * 2
        return comprimento_total + espacos_entre_vagoes

    def calcular_peso_total(self):
        # Calcula o peso total da composição.
        peso_total = 0
        for vagao in self._data:
            if vagao is not None:
                peso_total += vagao.peso
        return peso_total

    def contar_passageiros(self):
        # Conta o número total de passageiros na composição.
        total_passageiros = 0
        for vagao in self._data:
            if isinstance(vagao, Passageiro):
                total_passageiros += vagao.passageiros
        return total_passageiros

    def contar_carga_total(self):
        # Contabiliza a carga transportada pela composição.
        total_carga = 0
        for vagao in self._data:
            if isinstance(vagao, Carga):
                total_carga += vagao.carga
        return total_carga

    def verificar_potencia(self):
        # Verifica se a potência das locomotivas é suficiente.
        potencia_total = 0
        peso_total = self.calcular_peso_total()
        
        # Soma a potência de todas as locomotivas.
        for vagao in self._data:
            if isinstance(vagao, Locomotiva):
                potencia_total += vagao.potencia
        
        if peso_total == 0:
            return "Composição vazia"
        
        # Calcula a relação HP/Ton.
        relacao_hpt = potencia_total / peso_total
        hpt_minimo = 1.05
        
        if relacao_hpt >= hpt_minimo:
            return f"Potência suficiente. HPT atual: {relacao_hpt:.2f}"
        else:
            # Calcula quantas locomotivas adicionais são necessárias.
            potencia_necessaria = (hpt_minimo * peso_total) - potencia_total
            # Assume que locomotivas iguais têm 2500 HP (padrão).
            locomotivas_adicionais = int(potencia_necessaria / 2500) + 1
            return f"Potência insuficiente. HPT atual: {relacao_hpt:.2f}. Adicione {locomotivas_adicionais} locomotiva(s)."

    def diagnostico_composicao(self):
        # Método que utiliza todos os métodos de cálculo para diagnóstico completo.
        print("=== DIAGNÓSTICO DA COMPOSIÇÃO FERROVIÁRIA ===")
        
        # Número de vagões e tipos.
        total, locomotivas, passageiros, cargas = self.contar_vagoes()
        print(f"Total de vagões: {total}")
        print(f"Locomotivas: {locomotivas}")
        print(f"Vagões de passageiros: {passageiros}")
        print(f"Vagões de carga: {cargas}")
        
        # Comprimento e peso.
        comprimento = self.calcular_comprimento_total()
        peso = self.calcular_peso_total()
        print(f"Comprimento total: {comprimento} m")
        print(f"Peso total: {peso} toneladas")
        
        # Passageiros e carga.
        total_passageiros = self.contar_passageiros()
        total_carga = self.contar_carga_total()
        print(f"Total de passageiros: {total_passageiros}")
        print(f"Total de carga: {total_carga} toneladas")
        
        # Verificação de potência.
        resultado_potencia = self.verificar_potencia()
        print(f"Verificação de potência: {resultado_potencia}")
        
        print("=" * 45)

    def obter_dados_vagao(self, posicao):
        # Retorna os dados de um vagão em uma posição específica.
        if posicao == "primeiro":
            return self.peek()
        elif posicao == "ultimo":
            return self.top()
        else:
            return None