def acessarSite(estado, cidade):
    '''
    Utiliza requests e beautifulsoup para acessar o site através da cidade
    e estado passados como parametro. Retorna três listas com: Dias da semana,
    temperaturas máximas e mínimas. Também retorna um dicionário com essas informações.
    '''
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
    return dict, Dias, TempsMax, TempsMin

def criarGrafico(informacoes, opcao):
  '''
  Usa da biblioteca matplotlib, Com informações e uma opção passada pelo usuario 
  para criar um arquivo CSV (com pandas), é utilizado para gerar um gráfico 
  com matplotlib, que por sua vez é salvo como uma imagem com o tipo de gráfico da escolha.
  '''
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

  fig, ax = plt.subplots(figsize=(10, 5))
  plt.title('Gráfico de relação: Dias da semana x Temperatura máxima e minima')
  ax.set_xlabel("DIAS DA SEMANA")
  ax.set_ylabel("TEMPERATURA (em graus célsius)")
  if opcao == 'linhas':
      plt.plot(barras, colunasMax, color= "red", label='Temperatura máxima')
      plt.plot(barras, ColunasMin, color= "blue", label='Temperatura mínima')
      
  elif opcao == 'barras':
      ax.bar(barras, colunasMax, color= "red", label='Temperatura máxima')
      ax.bar(barras, ColunasMin, color= "blue", label='Temperatura nínima')
    
  plt.legend()
  plt.grid()  
  plt.savefig('graph.png')

def acharExtremos(dias, maximas, minimas):
    '''
    Usa das listas geradas em acessarSite para encontrar os dias mais quentes
    e mais frios para então coloca-los em listas que são retornadas.
    '''
    Dia_quente = max(maximas)
    Dia_frio = min(minimas)
    Dias_quentes = []
    Dias_frios = []
    
    for i, v in enumerate(maximas):
        if v == Dia_quente:
            Dias_quentes.append(dias[i])
    for i, v in enumerate(minimas):
        if v == Dia_frio:
            Dias_frios.append(dias[i])
            
    return Dias_quentes, Dias_frios

def analisarInformacoes(maximas, minimas):
    '''
    Calcula as médias das temperaturas e as retorna.
    '''
    mediaMax = sum(maximas)/len(maximas)
    mediaMin = sum(minimas)/len(minimas)
    mediaGeral = (mediaMax + mediaMin)/2
    return mediaMax, mediaMin, mediaGeral