from DequeVC import Deque
from Persistencia import Persistente
from Vagao import Vagao


class ComposicaoFerroviaria(Deque, Persistente):

    def __init__(self, N,nome_arquivo):
        Deque.__init__(self, N)
        Persistente.__init__(self,nome_arquivo)
        self.carregar()

    def criar_composicao_padrao(self):
        self.__data = [None]*self._N
        self._size = 0
        self._front = 0
        self._top = 0

        self.salvar()