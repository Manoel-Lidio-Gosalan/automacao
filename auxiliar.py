"""pegar localização do mouse"""
import time
import pyautogui as pag
import pandas as pd



time.sleep(5)
print(pag.position())

base = pd.read_csv('./produtos.csv')
print(base)
