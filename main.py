#Passos a serem seguidos

# 1 - Abrir o site/sistema da empresa 
# 2 - Realizar o login
# 3 - Importar a base de dados
# 4 - Cadastrar um produto
# 5 - Repetir esse processo até acabar a base

# Vamos primeiro importar as bibliotecas

import time
import pyautogui
import pandas as pd 

# Após isso vamos fazer o PyAutoGUI abrir o Chrome e acessar no site/sistema da empresa
pyautogui.PAUSE = 2
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
# Já abriu o Chrome, agora vamos entrar no sistema/site da empresa
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3.5) #Aqui dei uma pausa para evitar erros caso demore o carregamento da página

# Próximo passo é fazer nosso programar realizar o login no site. Então deve-se clicar nos campos corretamente, digitar e acessar a área de cadastro de produtos

# selecionar o campo de email
pyautogui.press("tab") # Deveria ser usado o .click com as coordenadas, mas para ser responsível todos os PC's, estou utilizando o TAB que funcionou igual, e sem depender da coordenada de cada monitor

# escrever o seu email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.press("tab") # clique no botao de login
pyautogui.press("enter") # clique no botao de login
time.sleep(2.5)

#Realizado o login, precisamos acessar a base de dados e usaremos o Pandas
tabela = pd.read_csv('produtos.csv')

#Já temos a planilha importada via Pandas, agora precisamo cadastrar cada um dos produtos

# Para cadastrar um produto utilizaremos o FOR, para ele percorrer por toda a planilha
for linha in tabela.index:
    # Selecionar o primeiro campo (código)
    pyautogui.press('tab')
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # No campo OBS temos um problema caso seja NaN e com esse comando, criamos uma condicional em que verificamos com o pd, se é ou não um NaN
    obs = tabela.loc[linha, "obs"] 
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)

    # Clicamos em qualquer lugar da tela para conseguirmos voltar para o primiro campo utilizando aquele primeiro 'tab
    pyautogui.click(x=241, y=583)

    # Passo 5: Repetir o processo de cadastro até o fim