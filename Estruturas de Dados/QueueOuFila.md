# Queue ou Fila
Essencialmente é FIFO
(First In, First Out - o primeiro a entrar é o primeiro a sair).

1,2,3 -> remove 1 -> 2,3 -> add 4 -> 2,3,4 -> remove 2 -> 3,4

É uma estrutura para fazer buffering ou streaming de dados.

Pode ser implementada de algumas maneiras, a mais comum e by-the-book usa liked list.

Precisa ter uma referência para o head (início) e tail (final) da fila.

O head é onde removemos os elementos (dequeue) e o tail é onde adicionamos novos elementos (enqueue).

## From queue to Dequeue (Double-Ended Queue)
De linked list para doubly linked list. Os elementos apontam uns para os outros também na ordem inversa.

Dessa forma podemos adicionar e remover elementos tanto do início quanto do final da fila.

Não é mais necessariamente FIFO, podemos usar como stack também (LIFO).

## Queue em Python
Python tem uma implementação pronta na biblioteca padrão, chamada `queue`.

Mas na verdade ela implementa os métodos da dequeue, no próprio método init da queue, é implementado uma dequeue internamente.

No fundo a dequeue não é implementada em python puro, é uma implementação em CPython.
Mas abrindo o código do CPython, vemos que é uma implementação simples de doubly linked list.


