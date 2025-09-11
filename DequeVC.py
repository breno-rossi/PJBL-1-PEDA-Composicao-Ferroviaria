# -- coding: latin-1 --

class Except(Exception):  #Tratamento de exceção personalizada. Uso: raise Except(<mensagem>)
    pass

class Deque:
    """
    Classe Deque: implementação utilizando lista/vetor estático circular.
    """

    def __init__(self, N):
        """
        Cria novo deque como lista de tamanho fixo: vetor estático.
        """

        self._N = N                    # Tamanho máximo do deque
        self._data = [None] * N        # Lista de tamanho máximo N
        self._size = 0                 # Tamanho corrente do deque
        
        # Frente (início) do deque: é decrementado/incrementado a cada addFirst()/deleteFirst(), respectivamente
        self._front = 0                # Posição inicial da frente/início
        
        # Top (final) do deque: é incrementado/decrementado a cada addLast()/deleteLast(), respectivamente
        self._top = 0                  # Posição corrente do topo/fim
        
        # Ponteiro utilizado para percorrer o deque
        self._ptr = 0                  # Posição do ponteiro no deque (0 no início)

    def isEmpty(self):
        """
        Retorna verdadeiro se o deque estiver vazio.
        
        Returns:
            bool: True se vazio, False caso contrário
        """
        return self._size == 0

    def isFull(self):
        """
        Retorna verdadeiro se o deque estiver cheio.
        
        Returns:
            bool: True se cheio, False caso contrário
        """
        return self._size == self._N

    def getSize(self):
        """
        Retorna o tamanho atual do deque.
        
        Returns:
            int: Número de elementos no deque
        """
        return self._size

    def peek(self):
        """
        Retorna None se o deque estiver vazio.
        Se não, retorna elemento no início do deque sem removê-lo.
        
        Returns:
            any: Primeiro elemento do deque ou None se vazio
        """
        if self.isEmpty():
            return None
        return self._data[self._front]  # Primeiro item do deque

    def top(self):
        """
        Retorna None se o deque estiver vazio.
        Senão, retorna elemento no fim do deque sem removê-lo.
        
        Returns:
            any: Último elemento do deque ou None se vazio
        """
        if self.isEmpty():
            return None
        else:
            return self._data[self._top]  # Último item do deque

    def __str__(self):
        """
        Representação em string do deque.
        
        Se o deque estiver vazio, retorna mensagem "Deque vazio";
        senão, monta uma lista temporária, define tamanho da lista temporária como zero,
        coloca o ponteiro livre no início do deque, percorre o deque até o final e
        adiciona cada elemento do deque na lista temporária,
        usa str(lista_temp) para retornar o string do deque.
        
        Returns:
            str: Representação do deque como string
        """
        if self.isEmpty():
            return "Deque vazio."
        else:
            lista_temp = []
            str_size = 0
            self.rewind()
            
            while str_size < self._size:
                lista_temp.append(self.next())
                str_size += 1
                
            return str(lista_temp)

    def getVC(self):
        """
        Retorna a string do vetor circular (str(lista)).
        
        Returns:
            str: Representação do vetor circular interno
        """
        return str(self._data)

    def rewind(self):
        """
        Coloca ponteiro no início do deque.
        """
        self._ptr = self._front

    def next(self):
        """
        Se lista vazia, retorna None;
        senão, guarda o elemento no ponteiro,
        avança o ponteiro uma posição, circulando se necessário,
        retorna o elemento guardado.
        
        Returns:
            any: Próximo elemento do deque ou None se vazio
        """
        if self.isEmpty():
            return None
        else:
            e = self._data[self._ptr]
            self._ptr += 1
            
            if self._ptr == self._N:  # Passou o fim do deque?
                self._ptr = 0         # Circula
                
            return e

    def addFirst(self, e):
        """
        Adiciona elemento no início do deque.
        
        Se deque cheio, lança exceção com mensagem.
        Se deque vazio, inicializa início (posição 0) com elemento,
        senão, decrementa o ponteiro para o início, circulando se necessário;
        adiciona elemento no novo início do deque.
        Aumenta o tamanho do deque.
        
        Args:
            e (any): Elemento a ser adicionado no início
            
        Raises:
            Except: Se o deque estiver cheio
        """
        if self.isFull():
            raise Except("O Deque está cheio")
        if self.isEmpty():
            self._data[self._front] = e
        else:
            self._front = (self._front - 1) % self._N
            self._data[self._front] = e

        self._size += 1


    def addLast(self, e):
        """
        Adiciona elemento no final do deque.
        
        Se deque cheio, lança exceção com mensagem.
        Se deque vazio, inicializa início (posição 0) com elemento.
        Senão, incrementa o ponteiro para o topo, circulando se necessário,
        adiciona elemento no novo topo do deque.
        Aumenta o tamanho do deque.
        
        Args:
            e (any): Elemento a ser adicionado no final
            
        Raises:
            Except: Se o deque estiver cheio
        """

        if self.isFull():
            raise Except("O Deque está cheio")
        if self.isEmpty():
            self._data[self._top] = e
        else:
            self._top += 1
            if self._top == self._N:  # Passou o fim do deque?
                self._top = 0         # Circula
            self._data[self._top] = e

        self._size += 1

    def deleteFirst(self):
        """
        Remove e retorna elemento do início do deque.
        
        Se deque vazio, lança exceção com mensagem,
        senão, guarda o elemento do início do deque,
        atribui None para a posição corrente do início,
        diminui o tamanho do deque,
        incrementa o ponteiro para o início, circulando se necessário,
        retorna o elemento guardado.
        
        Returns:
            any: Elemento removido do início do deque
            
        Raises:
            Except: Se o deque estiver vazio
        """
        if self.isEmpty():
            raise Except("O Deque está vazio")

        e = self._data[self._front]
        self._data[self._front] = None
        self._size -= 1
        self._front += 1

        if self._front == self._N:  # Passou o fim do deque?
            self._front = 0         # Circula

        return e

    def deleteLast(self):
        """
        Remove e retorna elemento do final do deque.
        
        Se deque vazio, lança exceção com mensagem,
        senão, guarda o elemento do topo do deque,
        atribui None para a posição corrente do topo,
        diminui o tamanho do deque,
        decrementa o ponteiro para o topo, circulando se necessário,
        retorna o elemento guardado.
        
        Returns:
            any: Elemento removido do final do deque
            
        Raises:
            Except: Se o deque estiver vazio
        """
        if self.isEmpty():
            raise Except("O Deque está vazio")

        e = self._data[self._top]
        self._data[self._top] = None
        self._size -= 1
        self._top -= 1

        if self._top < 0:  # Passou o início do deque?
            self._top = self._N - 1  # Circula

        return e
    