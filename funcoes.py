def acessarSite(estado, cidade):
    import requests
    from bs4 import BeautifulSoup

    link = f"https://g1.globo.com/previsao-do-tempo/{estado}/{cidade}.ghtml"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
    requisicao = requests.get(link, headers=headers)
    site = BeautifulSoup(requisicao.text, 'html.parser')
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
    return dict


def criarGrafico(informacoes, opcao):
  import pandas as pd
  import matplotlib as mpl
  import matplotlib.pyplot as plt
  mpl.use('Agg')

  df = pd.DataFrame(informacoes) 
  df.to_csv('temperaturas.csv')
  df = pd.read_csv('temperaturas.csv')
  barras = df["Dia"]
  colunasMax = df["Temperatura máxima"]
  ColunasMin = df["Temperatura mínima"]

  fig, ax = plt.subplots(figsize=(8, 5))
  # plt.title("GRÁFICO DE TEMPERATURA MÁXIMA E MÍNIMA")
  plt.title('Bom dia')
  ax.set_xlabel("DIAS DA SEMANA")
  ax.set_ylabel("TEMPERATURA")
  # ax.bar(barras, colunasMax, color= "red")
  # ax.bar(barras, ColunasMin, color= "blue")
  if opcao == 'linhas':
      plt.plot(barras, colunasMax, color= "red")
      plt.plot(barras, ColunasMin, color= "blue")
      
  elif opcao == 'barras':
      ax.bar(barras, colunasMax, color= "red")
      ax.bar(barras, ColunasMin, color= "blue")
      ax.bar_label(colunasMax, label_type='center')
  plt.savefig('graph.png')
