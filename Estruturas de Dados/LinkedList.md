# Linked List

Diferente de um array pois os elementos não estão armazenados sequencialmente na memória.

Não sabemos onde os outros elementos estão e o tamanho da lista.

Temos um ponteiro apontando para o item inicial (cabeça/head) da lista.

O primeiro elemento aponta para o segundo, o segundo para o terceiro e assim por diante...
Até o último que aponta para null (ou None em Python).

Se tivermos ponteiros para o próximo e o anterior, temos uma Doubly Linked List (lista duplamente ligada).
Ao invés de Singly Linked List (lista simplesmente ligada).

## Linked List vs Array
| Característica       | Linked List                                          | Array                                            |
|----------------------|------------------------------------------------------|--------------------------------------------------|
| Acesso / Leitura     | Sequencial (O(n)) ou Direto (O(1)) para head ou tail | Direto (O(1))                                    |
| Inserção/Remoção     | Rápida (O(1) se o ponteiro estiver disponível)       | Lenta (O(n) para manter a ordem)                 |
| Armazenamento        | Elementos não contínuos                              | Elementos contínuos                              |
| Tamanho              | Dinâmico                                             | Fixo (em arrays tradicionais)                    |


