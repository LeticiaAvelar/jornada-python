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

for mensagem in st.session_state["lista_mensagem"]: # percorre todas as mensagens salvas na lista de mensagens
    role = mensagem["role"] # pega o papel (role) de cada mensagem
    content = mensagem["content"] # pega o conteudo (content) de cada mensagem
    st.chat_message(role).write(content)
    # exibe cada mensagem na tela do app, usando o papel (role) e o conteudo (content) de cada mensagem
    

if texto_usuario: # o if verifica se o usuario digitou algo, se essa variavel não está vazia
    print(texto_usuario) # só é executado se a condição for verdadeira
    st.chat_message("user").write(texto_usuario) # exibe a mensagem do usuario na tela do app
    # podemos passar esse parâmetro de três formas: "user", "assistant", ou "nome personalizado"
    mensagem_usuario = {"role": "user", "content": texto_usuario} # cria um dicionário com a mensagem do usuario
    st.session_state["lista_mensagem"].append(mensagem_usuario) # adiciona a mensagem do usuario na lista de mensagens

    # ia respondeu
    resposta_ia = "Você perguntou: " + texto_usuario + "?" # resposta temporária da IA
    st.chat_message("assistant").write(resposta_ia) # exibe a resposta da IA na tela do app
    mensagem_ia = {"role": "assistant", "content": resposta_ia} # cria um dicionário com a resposta da IA
    st.session_state["lista_mensagem"].append(mensagem_ia) # adiciona a resposta da IA na lista de mensagens

# print(st.session_state["lista_mensagem"]) # mostra no terminal todas as mensagens trocadas no chat