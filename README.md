Criado com objetivo de tornar mais fácil a visualização de temperaturas ao longo da semana, VisaTempo é uma aplicação baseada em python com uso de Requests, BeautifulSoup, Pandas e Matplotlib, cada uma desempenhando seu papel ao longo do código.

Requests: A mais simples entre as quatro, envia alguns dados para um site que por sua vez lê os dados e caso esteja tudo certo, retorna informações que podem então ser utilizadas.

BeautifulSoup: Biblioteca de webscrapping responsável pela maior parte do código, cria um objeto e seu valor é atribuído baseado na informação recebida pelo requests, tratando um código HTML de diversas formas diferentes, no código, usado de forma relativamente simples.

Pandas: Biblioteca com diversos usos, porém, na aplicação, apenas usada para criação de um arquivo CSV (Comma separated values, Valores separados por vírgula)

Matplotlib: Biblioteca gráfica que utiliza os dados processados para criar diferentes tipos de gráficos. Constitui uma grande parte do código.

PARA QUE SERVE?
VisaTempo usa de programação para facilitar a vida do usuário que se preocupa com o clima, mais especificamente com a temperatura. Quão comumente viajamos para uma determinada região e somos pêgos de surpresa por uma sensação térmica diferente do que estamos acostumados? Um problema mais frequente do que se pensa, e um ao qual oferecemos a solução.

Com apenas poucas palavras digitadas, o usuario consegue ter acesso a um grafico elaborado de forma simples, que traduz o que programas meteorologicos ou o proprio site podem ter certa dificuldade em passar de forma clara, direta e consisa. 


MODO DE USO:
Após execução do código, o terminal irá requirir o input de algumas informações, sendo elas o estado e cidade a qual se pretende criar o gráfico a respeito. Com essas informações, a aplicação consegue acessar o dito site (G1) e retirar de seu html as informações que são úteis, processando para que se tornem mais legiveis e finalmente as retornando como listas e um dicionário. O programa então irá perguntar a respeito de que tipo de gráfico o usuário prefere criar, usando essa opção para definir o estilo do gráfico e transformá-lo em uma imagem com as temperaturas.

