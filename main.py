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

# Chamada de outra função para usar as listas de temperaturas e retornar listas com os nomes dos
# dias maais frios e os dias mais quentes.
Dias_quentes, Dias_frios = acharExtremos(Dias, TempMax, TempMin)

# Transforma as listas em uma string
Dias_quentes = ", ".join(Dias_quentes)
Dias_frios = ", ".join(Dias_frios)

# Chama a ultima função, utilizando as primeiras listas para calcular médias.
mediaMax, mediaMin, mediaGeral = analisarInformacoes(TempMax, TempMin)
print(f'Gráfico gerado com as informações da cidade!\nDia possivelmente mais quente: {Dias_quentes}\nDia possivelmente mais frio: {Dias_frios}')
print(f'A temperatura média é: {mediaGeral:.0f}°c\nA média maxima é: {mediaMax:.0f}°c\nE a média minima é: {mediaMin:.0f}°c')