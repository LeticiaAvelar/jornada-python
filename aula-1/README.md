# 🤖 Jornada Python — Aula 1 | Automação de Tarefas e Bots

Projeto desenvolvido durante a **Aula 1 da Jornada Python** do canal **Hashtag Treinamentos**, com foco em **automação de tarefas repetitivas usando Python**.

Nesta aula, o objetivo foi entender como criar **bots simples** que simulam ações humanas no computador para ganhar produtividade e reduzir erros manuais.

---

## 🧠 Conceitos abordados na aula

- O que é automação de tarefas
- Quando faz sentido automatizar processos
- Uso do Python para automações simples
- Controle de mouse e teclado com **PyAutoGUI**
- Leitura de dados com **Pandas**
- Automação de preenchimento de formulários

---

## 🚀 Sobre o projeto

Neste mini-projeto, desenvolvi um script que:

- Lê um arquivo **CSV** com dados previamente cadastrados
- Percorre linha por linha desses dados
- Simula ações de **mouse e teclado**
- Realiza o cadastro automático dos itens em um **site fictício**

O projeto simula um cenário real de tarefas manuais repetitivas, como cadastros administrativos ou operacionais.

---

## 🎥 Demonstração

[https://github.com/LeticiaAvelar/jornada-python/aula-1/demo.gif](https://github.com/LeticiaAvelar/jornada-python/blob/main/aula-1/demo.gif)

---

## 🛠 Tecnologias utilizadas

- **Python**
- **PyAutoGUI** → automação de mouse e teclado
- **Pandas** → leitura e manipulação do CSV

---

## 📂 Estrutura do projeto

📦 automacao-aula1

┣ 📄 dados.csv # Arquivo com os itens a serem cadastrados

┣ 📄 automacao.py # Script principal de automação

┗ 📄 README.md

---

## ⚙️ Pré-requisitos

Instale as bibliotecas necessárias:

```bash
pip install pyautogui pandas
```

⚠️ Atenção:
Durante a execução do script, não utilize mouse ou teclado, pois o bot assume o controle da tela. Lembre-se, os times deverão ser configurados de acordo com a máquina que fará uso.
