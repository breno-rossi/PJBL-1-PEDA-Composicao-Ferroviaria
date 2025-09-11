import pickle 
import os 

# Define a classe base que oferece persistência de dados para subclasses.
class Persistente:
	def __init__(self, nome_arquivo):
		# Construtor da classe Persistente.
		# Recebe o nome do arquivo onde os dados serão armazenados.
		# O atributo é protegido (_nome_arquivo), acessível por subclasses.
		self._nome_arquivo = nome_arquivo

	def salvar(self, dados):
		# Método que salva os dados fornecidos no arquivo especificado.
		# Os dados podem ser listas, dicionários, objetos ou outros tipos
		# serializáveis com pickle.
		try:
			# Abre o arquivo no modo binário de escrita ('wb').
			with open(self._nome_arquivo, 'wb') as arq:
				# Serializa os dados e grava no arquivo.
				pickle.dump(dados, arq)
			# Informa que os dados foram salvos com sucesso.
			print("Dados salvos em: " + self._nome_arquivo)
		except (pickle.PicklingError, PermissionError, OSError) as e:
			# Em caso de erro na serialização ou permissão, exibe a mensagem.
			print("Erro ao salvar arquivo '" + self._nome_arquivo + "':", e)

	def carregar(self):
		# Método que tenta carregar os dados de um arquivo, se ele existir.
		# Retorna os dados desserializados. Em caso de erro, retorna lista vazia.
		if os.path.exists(self._nome_arquivo):
			# Se o arquivo existir, tenta carregá-lo.
			try:
				# Abre o arquivo no modo binário de leitura ('rb').
				with open(self._nome_arquivo, 'rb') as arq:
					# Desserializa os dados do arquivo.
					dados = pickle.load(arq)
				# Informa que o carregamento foi realizado com sucesso.
				print("Arquivo '" + self._nome_arquivo +
					  "' carregado com sucesso.")
				return dados # Retorna os dados carregados.
			except (pickle.UnpicklingError, EOFError,
					PermissionError, OSError) as e:
				# Em caso de erro na leitura, exibe a mensagem e retorna lista vazia.
				print("Erro ao carregar arquivo '" + self._nome_arquivo + "':", e)
				return []
		else:
			# Se o arquivo não existir, informa e retorna lista vazia.
			print("Aviso: Arquivo '" + self._nome_arquivo +
				  "' não encontrado.")
			return []

##########################################################################
# Classe derivada que herda métodos de persistência e manipula uma lista.
# Dessa forma, a classe pode recuperar e salvar seus dados (a lista).
class MinhaClasse(Persistente):
	def __init__(self, nome_arquivo):
		# Inicializa a persistência com o nome do arquivo.
		super().__init__(nome_arquivo)
		# Tenta carregar a lista do arquivo.
		self.__lista = self.carregar()

	def obter_lista(self):
		# Retorna a lista atualmente armazenada.
		return self.__lista

	def atualizar_lista(self, nova_lista):
		# Substitui a lista e salva no arquivo.
		self.__lista = nova_lista
		self.salvar(self.__lista)

### PROGRAMA PRINCIPAL ###
# Cria a instância da classe que possui persistência herdada.
objeto = MinhaClasse('persistDados.pkl')
# Exibe a lista carregada (ou vazia).
print("Lista atual:", objeto.obter_lista())
# Atualiza com nova lista e persiste.
objeto.atualizar_lista([10, 20, 30, 40, 50])
# Exibe a lista atualizada.
print("Lista atualizada:", objeto.obter_lista())