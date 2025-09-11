# PJBL 1 - Aplicação de Deque em Composição Ferroviária

Este repositório contém o projeto desenvolvido para o trabalho da disciplina **Programação com Estruturas de Dados Avançadas** (PEDA), cujo objetivo é aplicar conceitos de Deque, Herança, Polimorfismo, Persistência e Herança Múltipla em Python para simular e gerenciar composições ferroviárias.

## Descrição do Projeto

O projeto consiste em implementar um sistema que permite criar, modificar, salvar e diagnosticar composições ferroviárias (trens), onde cada composição é estruturada como um **Deque** (fila dupla). O sistema gerencia diferentes tipos de vagões, utilizando conceitos de orientação a objetos e persistência de dados.

### Estrutura de Classes

- **Vagão (classe base):** Define atributos comuns a todos os vagões (comprimento, peso) e método `imprime()`.
- **Locomotiva, Passageiro, Carga (classes derivadas):** Herança da classe Vagão, cada uma com atributos e métodos específicos sobrescritos.
- **Persistente:** Classe base para persistência de dados via `pickle`, permitindo salvar e carregar composições em arquivos `.pkl`.
- **Deque:** Estrutura de dados implementada anteriormente na disciplina, utilizada para gerenciamento dinâmico dos vagões.
- **ComposiçãoFerroviaria:** Classe principal do projeto, derivada de `Deque` e `Persistente` (herança múltipla), responsável por toda a lógica de operações sobre a composição e integração das funcionalidades.

### Funcionalidades

- **Criação automática da composição padrão:** Gera uma composição inicial conforme especificação do anexo do trabalho.
- **Inserção e remoção de vagões:** Permite adicionar ou retirar vagões de ambos os extremos do deque, atualizando o arquivo de persistência automaticamente.
- **Diagnóstico da composição:** Calcula e apresenta estatísticas como número e tipo de vagões, comprimento total, peso, número de passageiros, carga transportada e relação potência/peso para verificar se a(s) locomotiva(s) são suficientes.
- **Consulta de dados de vagões:** Exibe informações detalhadas do primeiro e último vagão da composição.
- **Persistência automática:** Toda alteração é salva em arquivo binário para garantir integridade e continuidade dos dados entre execuções.

### Programa de Teste

O sistema dispõe de um menu interativo que permite ao usuário:
- Criar a composição padrão
- Inserir/remover vagões (frente/final, escolhendo tipo e atributos)
- Apresentar diagnóstico da composição
- Consultar informações do primeiro/último vagão
- Encerrar o programa

## Requisitos Técnicos

- **Python 3.x**
- Utilização obrigatória do módulo `pickle` para persistência
- Organização e modelagem conforme diagrama de classes fornecido no enunciado
- Não altere os métodos da classe Deque original; apenas utilize-os via herança

## Entrega

- **Arquivos obrigatórios:**
  - Código-fonte Python (`*.py`)
  - Arquivo de persistência da composição (`*.pkl`)

## Referências

- PUGA, Sandra Gavioli; RISSETTI, Gerson. *Lógica de programação e estruturas de dados, com aplicações em Java*. Pearson, 2016.
- GOODRICH, Michael T.; TAMASSIA, Roberto. *Estruturas de dados e algoritmos em Java*. Grupo A, 2013.
- SZWARCFITER, Jayme L.; MARKENZON, Lilian. *Estruturas de Dados e Seus Algoritmos*. LTC, 2010.

---

**Observação:** Este projeto é destinado exclusivamente para fins acadêmicos na disciplina PEDA. Para dúvidas sobre implementação, consulte o material de aula ou as referências sugeridas.
