# 🤖 Jornada Python — Aula 3 | Projeto de Previsão com Machine Learning

Projeto desenvolvido durante a **Aula 3 da Jornada Python** do canal **Hashtag Treinamentos**, com foco em **Machine Learning aplicado a problemas de negócio**.

Nesta aula, o objetivo foi construir um **modelo de Inteligência Artificial** capaz de analisar dados de clientes e **prever automaticamente o score de crédito**.

---

## 🧠 Contexto do projeto

### Case — Score de Crédito dos Clientes

Um banco precisa definir o **score de crédito** de seus clientes para apoiar decisões financeiras.  
O desafio foi criar um modelo que, a partir das informações do cliente, consiga classificá-lo como:

- **Ruim**
- **Ok**
- **Bom**

---

## 🚀 O que foi feito no projeto

Neste projeto, realizei:

- Leitura e exploração da base de dados
- Tratamento e preparação dos dados para Machine Learning
- Conversão de variáveis categóricas em numéricas
- Separação da base em treino e teste
- Criação e treinamento de múltiplos modelos de ML
- Avaliação da performance dos modelos
- Escolha do melhor modelo
- Previsão do score de novos clientes

---

## 🛠 Tecnologias utilizadas

- **Python**
- **Pandas** → manipulação de dados
- **Scikit-learn** → modelos de Machine Learning e métricas
- **LightGBM** → modelo baseado em gradient boosting
- **Jupyter Notebook** → desenvolvimento e análise

---

## 📂 Estrutura do projeto

📦 aula-3

┣ 📄 inicial.ipynb

┣ 📄 clientes.csv

┣ 📄 novos_clientes.csv

┗ 📄 README.md


---

## ⚙️ Pré-requisitos

Instale as bibliotecas necessárias:

```bash
pip install pandas scikit-learn lightgbm
```

⚠️ O projeto foi desenvolvido em Jupyter Notebook, utilizando display() para visualização dos dados.

---

## 🔎 Etapas do projeto
1️⃣ Entendimento do problema
- Definição do objetivo: prever o score de crédito do cliente com base em seus dados.

2️⃣ Preparação dos dados
- Leitura da base de clientes
- Análise dos tipos de dados
- Transformação de variáveis categóricas em numéricas usando LabelEncoder
- Remoção de colunas irrelevantes (id_cliente)

3️⃣ Separação de dados
- x → variáveis de entrada
- y → variável alvo (score_credito)
- Divisão da base em treino e teste

4️⃣ Criação dos modelos de Machine Learning
Foram testados três modelos:
- Random Forest (Árvore de Decisão)
- K-Nearest Neighbors (KNN)
- LightGBM (LGBMClassifier)

5️⃣ Avaliação dos modelos
- Os modelos foram comparados utilizando a métrica de acurácia.
- O modelo com melhor desempenho foi o Random Forest, sendo escolhido para uso final.

6️⃣ Previsão de novos clientes
Após a escolha do melhor modelo:
- Os dados de novos clientes foram tratados
- O modelo realizou a previsão automática do score de crédito

---

## 📈 Resultado

- O modelo final foi capaz de:
- Classificar clientes como Ruim, Ok ou Bom
- Automatizar a análise de crédito
- Apoiar decisões financeiras de forma escalável

---


## 📌 Observações

- Projeto com fins educacionais
- Base de dados utilizada apenas para estudo
- Abordagem introdutória a Machine Learning

---

## 📚 Aprendizados

- Preparação de dados para IA
- Importância da codificação de variáveis categóricas
- Comparação entre diferentes modelos de ML
- Avaliação de modelos com métricas

- Aplicação prática de Machine Learning em negócios
