# Bibliotecas = Pacotes de códigos prontos que podemos usar no nosso programa
# pyautogui = Biblioteca para automação de tarefas no computador
# pip install pyautogui # Comando para instalar a biblioteca pyautogui

import pyautogui
import time

pyautogui.PAUSE = 0.5  # Tempo de espera entre cada comando do pyautogui
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Passo 1: Entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(1)  # Espera o navegador abrir

# Passo 2: Fazer o login com meu usuário e senha
pyautogui.click(x=705, y=407)  # Clica no campo de usuário
pyautogui.write("pythonimpressionador@gmail.com")  # Digita o usuário
pyautogui.press("tab")  # Vai para o campo de senha
pyautogui.write("Hashtag@1234")  # Digita a senha
pyautogui.press("tab")  # Vai para o botão de login
pyautogui.press("enter")  # Clica no botão de login
time.sleep(1)  # Espera a página carregar

# Passo 3: Abrir a base de dados de produtos (importar a base de dados para o meu programa)
# pip install pandas openpyxl # Comando para instalar as bibliotecas pandas e openpyxl que permitem manipular arquivos Excel
import pandas as pd # Importa a biblioteca pandas para manipular dados com o apelido pd

tabela = pd.read_csv("Produtos.csv")  # Lê a tabela de produtos do arquivo CSV
print(tabela)  # Mostra a tabela no console

# Passo 4: Adicionar um novo produto à base de dados

# pyautogui.click(x=687, y=294)  # Clica no link da base de dados

# # CÓDIGO
# pyautogui.write("MOLO000251")  # Digita o código do produto
# pyautogui.press("tab")  # Vai para o campo de MARCA

# # MARCA
# pyautogui.write("Logitech")  # Digita a marca do produto
# pyautogui.press("tab")  # Vai para o campo de TIPO

# # TIPO
# pyautogui.write("Mouse")  # Digita o tipo do produto
# pyautogui.press("tab")  # Vai para o campo de CATEGORIA

# # CATEGORIA
# pyautogui.write("1")  # Digita a categoria do produto
# pyautogui.press("tab")  # Vai para o campo de PREÇO

# # PREÇO
# pyautogui.write("29.95")  # Digita o preço do produto
# pyautogui.press("tab")  # Vai para o botão de CUSTO

# # CUSTO
# pyautogui.write("6.5")  # Digita o custo do produto
# pyautogui.press("tab")  # Vai para o botão de OBSERVAÇÃO

# # OBSERVAÇÃO
# pyautogui.write("Mouse sem fio com nano receptor USB")  # Digita a observação do produto
# pyautogui.press("tab")  # Vai para o botão de ENVIAR

# pyautogui.press("enter")  # Clica no botão de ENVIAR

# Passo 5: Repetir o passo 4 para cada novo produto até acabar a lista

for linha in tabela.index:  # Para cada linha na tabela de produtos
    pyautogui.click(x=687, y=294)  # Clica no link da base de dados

    # CÓDIGO
    codigo = str(tabela.loc[linha, "codigo"])  # Pega o código do produto da linha atual
    pyautogui.write(codigo)
    pyautogui.press("tab")  # Vai para o campo de MARCA

    # MARCA
    marca = str(tabela.loc[linha, "marca"])  # Pega a marca do produto da linha atual
    pyautogui.write(marca)
    pyautogui.press("tab")  # Vai para o campo de TIPO

    # TIPO
    tipo = str(tabela.loc[linha, "tipo"])  # Pega o tipo do produto da linha atual
    pyautogui.write(tipo)
    pyautogui.press("tab")  # Vai para o campo de CATEGORIA

    # CATEGORIA
    categoria = str(tabela.loc[linha, "categoria"])  # Pega a categoria do produto da linha atual
    pyautogui.write(categoria)
    pyautogui.press("tab")  # Vai para o campo de PREÇO

    # PREÇO
    preco = str(tabela.loc[linha, "preco_unitario"])  # Pega o preço do produto da linha atual
    pyautogui.write(preco)
    pyautogui.press("tab")  # Vai para o botão de CUSTO

    # CUSTO
    custo = str(tabela.loc[linha, "custo"])  # Pega o custo do produto da linha atual
    pyautogui.write(custo)
    pyautogui.press("tab")  # Vai para o botão de OBSERVAÇÃO

    # OBSERVAÇÃO
    obs = str(tabela.loc[linha, "obs"])  # Pega a observação do produto da linha atual
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")  # Vai para o botão de ENVIAR

    pyautogui.press("enter")  # Clica no botão de ENVIAR
    pyautogui.scroll(2000)  # Sobe a tela para o topo da página