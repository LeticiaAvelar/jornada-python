# 🤖 Jornada Python — Aula 4 | Criação de Chatbot com IA em Tempo Real

Projeto desenvolvido durante a **Aula 4 da Jornada Python** do canal **Hashtag Treinamentos**, com foco na **criação de um chatbot com Inteligência Artificial**, utilizando **Streamlit** e a **API do Gemini**.

Nesta aula, o objetivo foi entender como funciona a lógica de um chat em tempo real, integrando frontend e backend em Python e mantendo o histórico da conversa com a IA.

---

## 🧠 Contexto do projeto

### Case — ChatBot Inteligente

O desafio foi criar um **chatbot funcional**, onde:

- o usuário envia mensagens em um chat
- a IA responde em tempo real
- todo o histórico da conversa é mantido
- a aplicação funciona de forma simples e interativa

O projeto simula um **chat com IA**, semelhante a aplicações reais usadas em atendimento, suporte ou assistentes virtuais.

---

## 🚀 O que foi feito no projeto

Neste projeto, realizei:

- Criação de interface de chat com Streamlit
- Implementação de input de mensagens do usuário
- Exibição do histórico completo da conversa
- Uso de listas e dicionários para estruturar mensagens
- Integração com a API da OpenAI
- Manutenção do estado da aplicação com `session_state`
- Separação de código principal e código auxiliar para aprendizado

---

## 🛠 Tecnologias utilizadas

- **Python**
- **Streamlit** → frontend e backend do chat
- **OpenAI API** → geração das respostas da IA
- **Listas e dicionários** → estruturação das mensagens

---

## 📂 Estrutura do projeto

📦 aula-4-chatbot-ia

┣ 📄 main.py  
┣ 📄 auxiliar.py  
┣ 📄 README.md  
┗ 🎥 demo.gif  

---

## ⚙️ Pré-requisitos

Instale as bibliotecas necessárias:

```bash
pip install streamlit openai
```

Para executar o projeto:
```bash
streamlit run main.py
```

## 🔎 Funcionamento do projeto

1️⃣ Interface do chat
- O Streamlit exibe o título do chatbot e o campo de entrada de mensagens.

2️⃣ Envio da mensagem
- Quando o usuário envia uma mensagem, ela é exibida no chat e armazenada em memória.

3️⃣ Histórico da conversa
- Todas as mensagens (usuário e IA) são guardadas em uma lista no session_state.

4️⃣ Resposta da IA
- O histórico completo é enviado para a API da OpenAI, permitindo respostas contextuais.

5️⃣ Exibição da resposta
- A resposta da IA aparece no chat e também é armazenada no histórico.

---

## 🧪 Arquivo auxiliar

O arquivo auxiliar.py foi utilizado para praticar conceitos fundamentais de Python, como:
- Manipulação de listas
- Uso de dicionários
- Estrutura de mensagens (role e content)
- Percorrer listas com for

Esses conceitos são a base para o funcionamento do chatbot.

---

## 🎥 Demonstração

![ChatBot com IA](aula-4/demo.gif)

---

O chat está funcionando online! Você pode testar no link abaixo:

[💬 Acesse o Chat no Streamlit](https://leticiaavelar-jornada-python-aula-4.streamlit.app/)

---

## 📌 Observações
- Projeto com foco educacional
- Chatbot criado para fins de aprendizado
- API utilizada apenas para testes
- Estrutura simples para facilitar o entendimento

---

## 📚 Aprendizados
- Como funciona a lógica de um chat com IA
- Integração de frontend e backend com Streamlit
- Importância do histórico de mensagens para respostas coerentes
- Uso prático de listas e dicionários em aplicações reais

- Primeiros passos na criação de aplicações com IA em Python
