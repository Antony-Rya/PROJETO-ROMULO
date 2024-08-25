from funcoes import *
print('##################################')
estado = input('Digite o estado: ').lower()
cidade = input('Digite a cidade: ').replace(" ", "-").lower()

informacoes = acessarSite(estado, cidade)

opcao = input('Que site tipo de grafico deseja criar?(Barras/Linhas): ').lower()

criarGrafico(informacoes, opcao)