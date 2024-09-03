from funcoes import *

# Coleta dos dados via input do usuário

estado = input('Digite o estado (Sigla): ').lower()
cidade = input('Digite a cidade: ').replace(" ", "-").lower()

# estado = 'pb'
# cidade = 'picui'


# Chamada da função, entregando as informações retiradas do input e atribuindo os resultados
# a 3 variáveis
informacoes, Dias, TempMax, TempMin = acessarSite(estado, cidade)

# Coleta de outra informação
opcao = input('Que site tipo de grafico deseja criar?(Barras/Linhas): ').lower()
# opcao = 'barras'

# Chamada da segunda função, entregando uma lista resultado da primeira função e o ultimo input.

criarGrafico(informacoes, opcao)

Dias_quentes, Dias_frios = acharExtremos(Dias, TempMax, TempMin)
Dias_quentes = ", ".join(Dias_quentes)
Dias_frios = ", ".join(Dias_frios)
mediaMax, mediaMin, mediaGeral = analisarInformacoes(TempMax, TempMin)
print(f'Gráfico gerado com as informações da cidade!\nDia possivelmente mais quente: {Dias_quentes}\nDia possivelmente mais frio: {Dias_frios}')
print(f'A temperatura média é: {mediaGeral:.0f}\nA média maxima é: {mediaMax:.0f}\nE a média minima é: {mediaMin:.0f}')