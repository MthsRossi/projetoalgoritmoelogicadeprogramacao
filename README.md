# 🏭 Sistema de Gestão de Peças – Automação Digital

## 📌 Descrição do Projeto

Este projeto foi desenvolvido como parte da disciplina de **Algoritmos e Lógica de Programação**, com o objetivo de simular um sistema de automação industrial para controle de produção e qualidade de peças.

A solução automatiza a análise de peças produzidas em uma linha de montagem, aplicando critérios de qualidade, classificando os itens e organizando o armazenamento das peças aprovadas em caixas com capacidade limitada.

---

## 🎯 Objetivo

Desenvolver um sistema em Python capaz de:

- Receber dados de peças produzidas
- Validar automaticamente critérios de qualidade
- Classificar peças como aprovadas ou reprovadas
- Armazenar peças aprovadas em caixas de até 10 unidades
- Gerar relatórios consolidados para análise

---

## ⚙️ Funcionalidades

### 🔹 Cadastro de Peças
O sistema permite cadastrar peças contendo:
- ID único
- Peso (em gramas)
- Cor
- Comprimento (em centímetros)

---

### 🔹 Validação Automática

Cada peça é avaliada com base nos seguintes critérios:

- Peso entre **95g e 105g**
- Cor **azul ou verde**
- Comprimento entre **10cm e 20cm**

Caso algum critério não seja atendido, a peça é reprovada e o sistema informa o motivo.

---

### 🔹 Classificação

- ✅ Peças aprovadas  
- ❌ Peças reprovadas (com justificativa detalhada)

---

### 📦 Armazenamento em Caixas

- Cada caixa comporta **até 10 peças aprovadas**
- Ao atingir o limite, a caixa é automaticamente fechada
- Uma nova caixa é iniciada automaticamente

---

### 📋 Menu Interativo

O sistema possui um menu com as seguintes opções:

1. Cadastrar nova peça  
2. Listar peças aprovadas/reprovadas  
3. Remover peça cadastrada  
4. Listar caixas fechadas  
5. Gerar relatório final  
0. Sair  

---

## ▶️ Como Executar o Projeto

### 1. Instalar o Python

Baixe e instale o Python 3:
https://www.python.org/

---

### 2. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git


### 3. Acessar a pasta do projeto
cd seu-repositorio

4. Executar o programa
python nome_do_arquivo.py

🧪 Exemplos de Uso

✔️ Exemplo de entrada válida
ID: 001
Peso: 100
Cor: azul
Comprimento: 15

✔️ Saída esperada
- Peça cadastrada com sucesso
- Status: Aprovada
- Motivo(s): Peça aprovada

❌ Exemplo de entrada inválida
- ID: 002
- Peso: 110
- Cor: vermelho
- Comprimento: 25

❌ Saída esperada
- Peça cadastrada com sucesso
- Status: Reprovada
- Motivo(s): Peso fora do padrão, Cor inválida, - Comprimento fora do padrão

📊 Relatório Final
- O sistema gera um relatório contendo:

- Total de peças cadastradas
- Total de peças aprovadas
- Total de peças reprovadas
- Motivos de reprovação
- Quantidade de caixas fechadas
- Peças na caixa atual

🧠 Estrutura do Sistema
- O sistema foi desenvolvido utilizando conceitos fundamentais de programação:

🔹 Funções
Separação de responsabilidades, como:

- Validação de peças
- Cadastro
- Organização das caixas
- Geração de relatórios

🔹 Estruturas Condicionais
- Uso de if/else para aplicar regras de validação.

🔹 Estruturas de Repetição
- while → controle do menu
- for → percorrer listas de peças

🔹 Estruturas de Dados
- Listas → armazenamento de peças
- Dicionários → organização dos dados de cada peça

🚀 Possíveis Melhorias
- O sistema pode ser expandido para um cenário real com:

- 💾 Integração com banco de dados (MySQL, SQLite)
- 🖥 Interface gráfica (Tkinter, PyQt)
- 📡 Integração com sensores industriais
- 🤖 Uso de inteligência artificial para análise de qualidade
- 📊 Dashboard para visualização em tempo real
- 🌐 Integração com sistemas ERP industriais

⚠️ Limitações do Projeto
- Os dados não são salvos permanentemente (memória temporária)
- Interface apenas via terminal
- Não há integração com hardware real

👨‍💻 Autor: Matheus Fernando Rossi

Disciplina: Algoritmos e Lógica de Programação
Curso: (coloque seu curso aqui)
Instituição: (coloque sua faculdade aqui)

📚 Referências

- https://docs.python.org/3/
- https://python.org.br/

Conteúdo da disciplina de Algoritmos e Lógica de Programação
