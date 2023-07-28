"""automação de tarefas"""
import time
import pyautogui as pag
import pandas as pd

# passo a passo do projeto
# 1 - Entrar no sistema da empresa)
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o navegador

pag.PAUSE = 1 #pausa de 1 segundo definido como regra as letras maiculas

pag.press('win')
time.sleep(1)
pag.write('opera')
pag.press('enter')


#entrar no link

time.sleep(2) #esperar 2 segundos esperar apenas dois segundospara realizar a acao seguinte

pag.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pag.press('enter')

time.sleep(2)

# 2 - fazer login com os dados informados

pag.click(x= 756, y= 354,)
pag.write('devgosalan@gmail.com')
pag.press('tab')
pag.write('123456')
pag.press('enter')

# 3 - importar a base de dados

tabela = pd.read_csv('./produtos.csv')

# 4 - cadastrar o produto
time.sleep(0.1)

LINHA = 0

for LINHA in tabela.index:

    pag.click(x=623, y=242)

    codigo = tabela.loc[LINHA,'codigo']
    pag.write(str(codigo))

    # 5 - peretir o processo para os demais produtos até cadastrar todos

    pag.press('tab')
    pag.write(str(tabela.loc[LINHA,'marca']))
    pag.press('tab')
    pag.write(str(tabela.loc[LINHA,'tipo']))
    pag.press('tab')
    pag.write(str(tabela.loc[LINHA,'categoria']))
    pag.press('tab')
    pag.write(str(tabela.loc[LINHA,'preco_unitario']))
    pag.press('tab')
    pag.write(str(tabela.loc[LINHA,'custo']))
    pag.press('tab')
    obs = tabela.loc[LINHA,'obs']
    if not pd.isna(obs):
        pag.write(str(tabela.loc[LINHA,'obs']))
    pag.press('tab')
    pag.press('enter')

    time.sleep(1)
    pag.scroll(2000)
