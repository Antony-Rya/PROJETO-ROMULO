from funcoes import *

# estado = input('Digite o estado (Sigla): ').lower()
# cidade = input('Digite a cidade: ').replace(" ", "-").lower()

estado = 'pb'
cidade = 'picui'

informacoes = acessarSite(estado, cidade)

# opcao = input('Que site tipo de grafico deseja criar?(Barras/Linhas): ').lower()
opcao = 'barras'
criarGrafico(informacoes, opcao)

Dias_quentes, Dias_frios = acharExtremos(informacoes)
Dias_quentes = ", ".join(Dias_quentes)
Dias_frios = ", ".join(Dias_frios)
print(f'Gráfico gerado com as informações da cidade!\nDia possivelmente mais quente: {Dias_quentes}\nDia possivelmente mais frio: {Dias_frios}')