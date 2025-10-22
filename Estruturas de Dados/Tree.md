# Binary Tree

```plaintext
        A
       / \
      B   C
     / \   \
    D   E   F
```

A Binary Tree tem um node com um valor (A), e dois ponteiros para outros nodes, esquerda (B) e direita (C).

O primeiro node é chamado de head ou root da árvore.
Cada node pode ter no máximo dois filhos (left e right), mas pode ter menos (inclusive nenhum).

É como uma linked list que diverge em dois caminhos a cada node.
Então, entendendo linked lists, estamos a um passo de entender árvores binárias.

A parte mais interessante é quando vemos os algoritmos que podemos usar em binary trees, como depth-first search (DFS) e breadth-first search (BFS).

## Outros tipos de Trees

### General Tree
Uma tree é uma também tem nodes conectados por arestas (edges), mas não tem a restrição de dois filhos por node.
Cada node contém um valor e pode ter múltiplos filhos (children).
A tree tem um node raiz (root) e cada node pode ter zero ou mais filhos.

### B-Tree (Balanced Tree)
Uma B-Tree é uma árvore auto-balanceada que mantém dados ordenados e permite buscas, inserções e deleções em tempo logarítmico.
Cada node pode ter mais de dois filhos, e a árvore é mantida balanceada para garantir eficiência nas operações.
Ela é amplamente usada em sistemas de banco de dados e sistemas de arquivos.
Ela segue algumas regras específicas para manter o balanceamento e a ordem dos dados.
- Número de chaves (keys) da B-tree
- O número de filhos (children) sempre vai ser o número de chaves + 1.
- Todas as folhas (leaves), ou últimos nodes da árvore, estão no mesmo nível.

### Heap
Uma Heap é uma árvore binária completa que satisfaz uma propriedade de heap (não as duas ao mesmo tempo):
- Max-Heap: O valor de cada node é maior ou igual ao valor de seus filhos.
- Min-Heap: O valor de cada node é menor ou igual ao valor de seus filhos.
Heaps são frequentemente usadas para implementar filas de prioridade.

