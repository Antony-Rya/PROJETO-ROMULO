#importação das bibliotecas
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
# from funcoes import *
mpl.use('Agg')
df = pd.read_csv('temperaturas.csv')

#Atribuição do link da página


estado = input('Digite o estado: ').lower()
cidade = input('Digite a cidade: ').replace(" ", "-").lower()

link = f"https://g1.globo.com/previsao-do-tempo/{estado}/{cidade}.ghtml"

#Definição da header
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}

#Utilização do requests para acesasr o link e requirir acesso ai html
requisicao = requests.get(link, headers=headers)
#Requirimento
print(requisicao)

#Uso do BeautifulSoup para criar uma variavel chamada "site" que vai guardar o objeto da sopa, passado pelo parser
site = BeautifulSoup(requisicao.text, "html.parser")

#Temperatura maxima e minima recebem todas as ocorrencias das Divs com essas classes, criando mais dois objetos

resumo = site.find_all('p', class_='forecast-header__summary')

Temps_proximos_dias = site.find_all("span", class_="forecast-next-days__item-value")
Nomes_proximos_dias = site.find_all("span", class_="forecast-next-days__item-label")
Dias = []
TempsMax = []
TempsMin = []
for dia in Nomes_proximos_dias:
    Dias.append(dia.get_text().replace(" ", "").replace("*", ""))
    if len(Dias) == 7:
        break

cont = 0
for temp in Temps_proximos_dias:
    
    temp = int(temp.get_text().replace(" ", "").replace("º", ""))
    if cont % 2 == 0:
        TempsMax.append(temp)
        
    else:
        TempsMin.append(temp)
        
    cont += 1
    if cont == 14:
        break



dict = {'Dia': Dias, 'Temperatura máxima': TempsMax, 'Temperatura mínima': TempsMin}  
df = pd.DataFrame(dict) 
df.to_csv('temperaturas.csv') 

def criarGrafico():
  barras = df["Dia"]
  colunasMax = df["Temperatura máxima"]
  ColunasMin = df["Temperatura mínima"]

  fig, ax = plt.subplots(figsize=(8, 5))
  # plt.title("GRÁFICO DE TEMPERATURA MÁXIMA E MÍNIMA")
#   plt.title(f"Dia atual: {Dias[0]}, clima: {resumo[0].get_text()}")
  plt.title(f"Cidade: {cidade}")
  ax.set_xlabel("DIAS DA ")
  ax.set_ylabel("TEMPERATURA")
  # ax.bar(barras, colunasMax, color= "red")
  # ax.bar(barras, ColunasMin, color= "blue")
  plt.plot(barras, colunasMax, color= "red")
  plt.plot(barras, ColunasMin, color= "blue")
  plt.savefig('graph.png')
  
  
  
# criarGrafico()


