# Trie ou Prefix-Tree

Conforme vamos avançando os nodes na árvore, vamos mantendo o prefixo da string que estamos formando.

Uma Trie é uma estrutura de dados em forma de árvore usada para armazenar um conjunto dinâmico ou um dicionário onde as chaves são geralmente strings.

Ela é usada em auto-complete, correção ortográfica, e outras aplicações que envolvem buscas rápidas por prefixos.

Exemplo de Trie armazenando as palavras: "cat", "car", "cart", "cog", "dog", "dove".

```plaintext
         (root)
        /      \
      c         d
     / \       / \
    a   o     o   o
   / \   \     \   \
  t   r   g     v   g
       \         \
        t         e
```

A explicação é até simples, mas a implementação dela é complexa.
Não é tão comum ver encontrar essa estrutura de dados, mas precisamos entender como ela funciona.

