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

- Cadastro de peças (ID, peso, cor, comprimento)
- Validação automática:
  - Peso entre 95g e 105g
  - Cor azul ou verde
  - Comprimento entre 10cm e 20cm
- Armazenamento em caixas (10 peças por caixa)
- Menu interativo
- Relatórios completos

---

## ▶️ Como executar

1. Instale o Python 3
2. Execute:

```
python programa.py
```

---

## 🧪 Exemplo

Entrada:
ID: 001
Peso: 100
Cor: azul
Comprimento: 15

Saída:
Peça aprovada

---

## 📊 Relatório
O sistema gera um relatório contendo:

- Total de peças cadastradas
- Total de peças aprovadas
- Total de peças reprovadas
- Motivos de reprovação
- Quantidade de caixas fechadas
- Peças na caixa atual


---

## 🚀 Melhorias futuras
O sistema pode ser expandido para um cenário real com:

- 💾 Integração com banco de dados (MySQL, SQLite)
- 🖥 Interface gráfica (Tkinter, PyQt)
- 📡 Integração com sensores industriais
- 🤖 Uso de inteligência artificial para análise de qualidade
- 📊 Dashboard para visualização em tempo real
- 🌐 Integração com sistemas ERP industriais

---

## 👨‍💻 Autor

Matheus Fernando Rossi

Disciplina: Algoritmos e Lógica de Programação
Curso: (coloque seu curso aqui)
Instituição: (coloque sua faculdade aqui)
