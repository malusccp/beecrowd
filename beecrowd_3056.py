# Paulo foi contratado por uma companhia de mapas digitais para implementar melhorias em seus mapas. Seu primeiro trabalho na empresa é
# implementar o algoritmo denominado deslocamento do ponto do meio. Não vamos descrever aqui o algoritmo completo, vamos focar apenas num aspecto 
# importante para Paulo, que está preocupado em otimizar o uso de memória em sua implementação do algoritmo. O algoritmo funciona em passos.
# Inicialmente, quatro pontos do mapa são selecionados, formando um quadrado. Então a cada passo, para cada quadrado, faça:

# • adicione quatro novos pontos, um ponto em cada lado do quadrado, exatamente no meio do lado.

# • adicione também mais um novo ponto, exatamente no meio do quadrado.

# O algoritmo utiliza os pontos criados para calcular e armazenar valores do mapa, mas Paulo está interessado apenas no número de pontos
# criados pelo algoritmo. Na figura abaixo, pontos brancos representam pontos adicionados no passo corrente, pontos pretos representam pontos
# adicionados em passos anteriores.


# Paulo notou que o algoritmo gera muitos pontos, e muitos pontos pertencem a mais de um quadrado. Para economizar memória, Paulo planeja 
# calcular e armazenar cada ponto apenas uma vez. Sua tarefa, dado o número de passos que Paulo planeja executar, é determinar a quantidade de 
#  pontos únicos que Paulo necessita calcular e armazenar.

# Entrada
# A entrada consiste de uma única linha que contém um inteiro N, o número de passos.

# Saída
# Seu programa deve produzir uma única linha, com apenas um número inteiro, a quantidade de pontos únicos que Paulo deve calcular e armazenar em N 
# passos.

# Restrições
# • 1 ≤ N ≤ 50
# Informações sobre a pontuação
# • Para um conjunto de casos de testes valendo 10 pontos, N ≤ 3. • Para um conjunto de casos de testes valendo outros 40 pontos, 4 ≤ N ≤ 10.