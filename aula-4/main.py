# exibir um titulo
# input do chat (campo de mensagem que o usuário digita)
# a cada mensagem que o usuario enviar:
    # mostrar a mensagem que o usuario enviou na tela
    # pegar a pergunta do usuario e enviar para a IA
    # receber a resposta da IA e exibir na tela

# as principais ferramentas de criação de ferramentas web em python são:
    # Streamlit (é a mais simples, ele é focado em criação de dashboards e apps simples, é dinamico e rápido de usar)
    # Flast (é um micro framework, mais flexível que o Streamlit, mas exige mais configuração inicial)
    # Django (é um framework completo, usado para aplicações maiores e mais complexas, com muitas funcionalidades prontas)
    # FastAPI (é focado em criação de APIs, é muito rápido e moderno, mas não é tão simples para iniciantes)

# NÓS VAMOS UTILIZAR O STREAMLIT, pois só com ele (com Python) já conseguimos fazer um app de chat simples e funcional, com frontend e backend integrados

# podemos usar qualquer IA na nossa aplicação (OpenAI, Gemini, Claude, Grok, etc), mas vamos usar a OpenAI, pois é a mais conhecida e tem uma documentação muito boa

# precisamos instalar o pacote do streamlit e da openai (que permite conectar com a API da OpenAI)
    # pip install streamlit openai

import streamlit as st

st.title("Fala que eu te escuto")

# para poder rodar a aplicação, usamos o comando no terminal:
    # streamlit run main.py

if not "lista_mensagem" in st.session_state:
    st.session_state["lista_mensagem"] = [] # cria uma lista de mensagem vazia APENAS na primeira vez que o app for carregado

texto_usuario = st.chat_input("Digite sua mensagem")
# arquivo_usuario = st.file_uploader("Envie um arquivo") # exemplo de upload de arquivo (não vamos usar nesse projeto)

if texto_usuario: # o if verifica se o usuario digitou algo, se essa variavel não está vazia
    print(texto_usuario) # só é executado se a condição for verdadeira
    st.chat_message("user").write(texto_usuario) # exibe a mensagem do usuario na tela do app
    # podemos passar esse parâmetro de três formas: "user", "assistant", ou "nome personalizado"

    # ia respondeu
    resposta_ia = "Você perguntou: " + texto_usuario + "?" # resposta temporária da IA
    st.chat_message("assistant").write(resposta_ia) # exibe a resposta da IA na tela do app