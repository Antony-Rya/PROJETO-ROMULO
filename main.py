from funcoes import *

# estado = input('Digite o estado (Sigla): ').lower()
# cidade = input('Digite a cidade: ').replace(" ", "-").lower()

estado = 'pb'
cidade = 'picui'

informacoes = acessarSite(estado, cidade)

# opcao = input('Que site tipo de grafico deseja criar?(Barras/Linhas): ').lower()
opcao = 'barras'
criarGrafico(informacoes, opcao)

Dia_quente, Dia_frio = acharExtremos(informacoes)

print(f'Gráfico gerado com as informações da cidade!\nDia possivelmente mais quente: {Dia_quente}\nDia possivelmente mais frio: {Dia_frio}')