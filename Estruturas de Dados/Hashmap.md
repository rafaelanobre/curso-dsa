# Hashmap

Dictionaries do Python são implementações de hashmaps.

Uma estrutura com uma função que acessa uma chave.
Essa chave mapeia um valor.

Na maioria dos casos, acessar um valor via chave é O(1).
Mesmo com milhares de elementos, o tempo médio de acesso é O(1).

A mágica para encontrar um valor de uma estrutura sem precisar percorrer todos os elementos é a função hash.

## Hash Function ou Hashing Function
Podemos encontrar um valor em um array em complexidade O(1) se soubermos o índice do elemento.

A hash function é uma função que transforma uma chave em um íncide de array através de um cálculo matemático.
A hash function deve sempre retornar o mesmo índice para a mesma chave.

Ela pode usar SHA-256, MD5 ou qualquer outro algoritmo de hash.
Esses algoritmos devolvem um número muito grande, então o número é reduzido para o tamanho do array usando o operador módulo (%).

## Load Factor
O load factor é a razão(diferença de tamanho) entre o número de elementos armazenados e o tamanho do array.
Um load factor alto indica que a tabela hash está cheia, o que pode levar a mais colisões e diminuir a eficiência.
Um load factor baixo indica que há espaço suficiente na tabela hash, o que pode melhorar a eficiência.

Precisamos monitorar o load factor para otimizar o desempenho.
Quando o load factor ultrapassa (geralmente) 0.7, ou seja, 70% do array preenchido.
Dobramos o tamanho do array (geralmente) e todos os elementos são re-hashados para o novo array.
Essa operação é custosa, então deve ocorrer raramente, para garantir o tempo médio de acesso permanece O(1).

## Colisões
Duas chaves diferentes podem gerar o mesmo índice. Isso é chamado de colisão.
Existem várias técnicas para lidar com colisões, como encadeamento (chaining) e endereçamento aberto (open addressing).

É importante entender que o hashmap guarda pares chave-valor na memória, e não apenas valores.
Assim mesmo que duas chaves diferentes gerem o mesmo índice, podemos encontrar o valor correto verificando a chave.

### Encadeamento (Chaining) - mais comum
Cada índice do array aponta para uma linked list ou outra estrutura de dados que armazena todos os pares chave-valor que colidiram naquele índice.
Quando ocorre uma colisão, o novo par chave-valor é simplesmente adicionado à linked list naquele índice.
Para buscar um valor, percorremos a linked list até encontrar a chave desejada.

### Endereçamento Aberto (Open Addressing) - menos comum
Quando ocorre uma colisão, a função hash procura o próximo índice disponível no array para armazenar o par chave-valor.
Existem várias estratégias para encontrar o próximo índice, como linear probing, quadratic probing e double hashing.
Para buscar um valor, a função hash verifica os índices subsequentes até encontrar a chave desejada ou um índice vazio.
Isso pode levar a O(n) no pior cenário, mas com um bom load factor, o desempenho médio ainda pode ser O(1).






