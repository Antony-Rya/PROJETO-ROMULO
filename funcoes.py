import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('Agg')
df = pd.read_csv('temperaturas.csv')

def criarGrafico():
  from main import Dias, resumo
  barras = df["Dia"]
  colunasMax = df["Temperatura máxima"]
  ColunasMin = df["Temperatura mínima"]

  fig, ax = plt.subplots(figsize=(8, 5))
  # plt.title("GRÁFICO DE TEMPERATURA MÁXIMA E MÍNIMA")
  plt.title(f"Dia atual: {Dias[0]}, clima: {resumo[0].get_text()}")
  ax.set_xlabel("DIAS DA SEMANA")
  ax.set_ylabel("TEMPERATURA")
  # ax.bar(barras, colunasMax, color= "red")
  # ax.bar(barras, ColunasMin, color= "blue")
  plt.plot(barras, colunasMax, color= "red")
  plt.plot(barras, ColunasMin, color= "blue")
  plt.savefig('graph.png')
