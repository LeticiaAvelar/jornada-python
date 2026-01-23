# 📊 Jornada Python — Aula 2 | Analisando Dados com Python

Projeto desenvolvido durante a **Aula 2 da Jornada Python** do canal **Hashtag Treinamentos**, com foco em **análise de dados usando Python**.

Nesta aula, o objetivo foi entender como explorar uma base de dados real, identificar problemas, gerar insights e apoiar decisões de negócio a partir dos dados.

---

## 🧠 Contexto do projeto

### Case — Cancelamento de Clientes

Uma empresa com mais de **800 mil clientes** percebeu que grande parte da sua base está inativa, ou seja, clientes que **cancelaram o serviço**.

O desafio do projeto foi:
- entender **os principais motivos dos cancelamentos**
- identificar **padrões de comportamento**
- sugerir **ações práticas** para reduzir o churn

---

## 🚀 O que foi feito no projeto

Neste projeto, realizei:

- Importação e leitura da base de dados em CSV
- Limpeza e tratamento dos dados
- Remoção de colunas irrelevantes
- Tratamento de valores nulos
- Análise exploratória dos dados
- Criação de gráficos interativos
- Identificação de causas de cancelamento
- Simulação de ações para reduzir o churn

---

## 🛠 Tecnologias utilizadas

- **Python**
- **Pandas** → manipulação e análise de dados
- **Plotly** → visualização de dados interativa
- **Jupyter Notebook** → análise exploratória

---

## 📂 Estrutura do projeto

📦 aula-2

┣ 📄 analise_cancelamentos.ipynb

┣ 📄 cancelamentos.csv

┗ 📄 README.md

---

## ⚙️ Pré-requisitos

Instale as bibliotecas necessárias:

```bash
pip install pandas openpyxl ipykernel nbformat plotly
```

⚠️ O uso de display() e gráficos interativos funciona corretamente em Jupyter Notebook (.ipynb).

---

## 🔎 Etapas da análise
1️⃣ Importação da base de dados

Leitura do arquivo CSV contendo informações dos clientes.

2️⃣ Exploração inicial

Análise das colunas, tipos de dados e identificação de informações irrelevantes.

3️⃣ Limpeza dos dados

- Remoção da coluna de ID
- Exclusão de linhas com valores nulos
- Ajuste da base para análise

4️⃣ Análise de cancelamento

- Contagem de clientes ativos vs cancelados
- Análise percentual do churn

5️⃣ Análise visual

Criação de gráficos para entender como cada variável impacta o cancelamento dos clientes.

---

## 📈 Principais insights encontrados

- Clientes com contrato mensal apresentaram taxa de cancelamento muito alta
- Clientes que ligaram mais de 4 vezes para o call center tendem a cancelar
- Clientes com mais de 20 dias de atraso no pagamento também cancelaram em massa

---

## 💡 Ações simuladas para reduzir cancelamentos

Com base nos dados, foram simuladas as seguintes ações:
- Incentivar planos anuais e trimestrais
- Resolver problemas do cliente em até 3 ligações
- Criar políticas para resolver atrasos em até 10 dias
- Após aplicar esses filtros, a taxa de cancelamento foi significativamente reduzida

---

## 🎥 Demonstração

![Análise de Dados](demo.gif)

---

## 📌 Observações

- Projeto com foco educacional
- Base de dados utilizada apenas para estudo
- Análise realizada com abordagem exploratória

---

## 📚 Aprendizados

- Importância da limpeza dos dados
- Como dados mal tratados afetam análises
- Uso de gráficos para apoiar decisões
- Transformar dados em ações de negócio

