# 🏭 Sistema de Gestão de Peças – Automação Digital

## 📌 Descrição do Projeto

Este projeto foi desenvolvido como parte da disciplina de **Algoritmos e Lógica de Programação**, com o objetivo de simular um sistema de automação industrial para controle de produção e qualidade de peças.

A solução automatiza a análise de peças produzidas em uma linha de montagem, aplicando critérios de qualidade, classificando os itens e organizando o armazenamento das peças aprovadas em caixas com capacidade limitada.

---

## 🎯 Objetivo

- Receber dados de peças produzidas  
- Validar automaticamente critérios de qualidade  
- Classificar peças como aprovadas ou reprovadas  
- Armazenar peças aprovadas em caixas de até 10 unidades  
- Gerar relatórios consolidados  

---

## ⚙️ Funcionalidades

### 🔹 Cadastro de Peças
- ID único  
- Peso (em gramas)  
- Cor  
- Comprimento (em centímetros)  

### 🔹 Validação Automática
- Peso entre **95g e 105g**  
- Cor **azul ou verde**  
- Comprimento entre **10cm e 20cm**  

### 🔹 Classificação
- Peças aprovadas  
- Peças reprovadas (com motivo)  

### 📦 Armazenamento em Caixas
- Cada caixa comporta **até 10 peças aprovadas**  
- Fechamento automático ao atingir o limite  

### 📋 Menu Interativo
1. Cadastrar nova peça  
2. Listar peças  
3. Remover peça  
4. Listar caixas fechadas  
5. Gerar relatório  
0. Sair  

---

## ▶️ Como Executar

1. Instale o Python 3  
2. Execute:

```
python nome_do_arquivo.py
```

---

## 🧪 Exemplos

### Entrada válida
ID: 001  
Peso: 100  
Cor: azul  
Comprimento: 15  

### Saída
Peça aprovada  

---

## 📊 Relatório Final

- Total de peças cadastradas  
- Total de peças aprovadas  
- Total de peças reprovadas  
- Motivos de reprovação  
- Quantidade de caixas fechadas  

---

## 🧠 Estrutura do Sistema

- Funções  
- Condicionais (if/else)  
- Repetições (for/while)  
- Listas e dicionários  

---

## 🚀 Possíveis Melhorias

- Banco de dados  
- Interface gráfica  
- Sensores industriais  
- Inteligência artificial  

---

## ⚠️ Limitações

- Dados não persistem  
- Interface apenas em terminal  

---

## 👨‍💻 Autor

Matheus  
Disciplina: Algoritmos e Lógica de Programação  
