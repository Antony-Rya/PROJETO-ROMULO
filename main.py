from funcoes import *

# estado = input('Digite o estado (Sigla): ').lower()
# cidade = input('Digite a cidade: ').replace(" ", "-").lower()

estado = 'pb'
cidade = 'picui'

informacoes = acessarSite(estado, cidade)

# opcao = input('Que site tipo de grafico deseja criar?(Barras/Linhas): ').lower()
opcao = 'barras'
# criarGrafico(informacoes, opcao)
print(len(informacoes))
# print('Gráfico gerado com as informações da cidade!\nDia possivelmente mais quente: ')