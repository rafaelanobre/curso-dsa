# Stack ou Pilha

Uma pilha, onde os itens são adicionados e removidos do topo da pilha, "um em cima do outro".

Princípio LIFO (Last In, First Out - o último a entrar é o primeiro a sair).


Se soubermos o tamanho máximo da pilha, podemos usar um array e um ponteiro para implementar a pilha.

Com a implementação de array, adicionar (push) e remover (pop) elementos são operações O(1).
Ela não garante que a nossa pilha possa crescer indefinidamente e isso é uma propriedade importante da pilha que queremos preservar.

```python
class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1
    def is_empty(self):
        return self.top == -1
    def is_full(self):
        return self.top == self.capacity - 1
    def push(self, value):
        if self.is_full():
            raise IndexError("push to full stack")
        self.top += 1
        self.stack[self.top] = value
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_value = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return popped_value
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[self.top]
```


Tradicionalmente, pilhas são implementadas usando linked lists.

Iniciamos o primeiro item (O(1)) e cada novo item é adicionado no topo da pilha (O(1)) usando o head da linked list como o topo da pilha.
Cada novo item aponta para o item que estava no topo da pilha anteriormente.

Remover um item do topo da pilha (pop) também é O(1), basta mover o head da linked list para o item abaixo do topo atual e retornar o valor do item que estava no topo.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def is_empty(self):
        return self.top is None
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.value
```
Essa implementação de pilha usando linked list permite que a pilha cresça dinamicamente conforme necessário, sem um tamanho máximo fixo.