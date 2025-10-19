# Big O Notation
`O(1) < O(log n) < O(sqrt(n)) < O(n) < O(n log n) < O(n²) < O(2^n) < O(n!)`

## O que é Big O?
É uma notação que fala sobre **escalabilidade** com o tamanho do input, não necessariamente a performance.

Nem sempre um algoritmo O(n) é mais rápido que o O(n²), precisamos fazer uma _análise assintótica_ para poder afirmar isso.

Mas O(n) na teoria é melhor que O(n²), por isso é preferível.

Big O não faz diferença com inputs pequeno, como um array com menos de 10 elementos, ele faz diferença em elementos grandes.

Quase sempre **consideramos o pior cenário** do algoritmo para medir a complexidade.

## Para que serve Big O?
Para medir a complexidade temporal e a complexidade espacial de um algoritmo.

**Complexidade temporal** é o tempo de execução ou runtime do nosso algoritmo.

**Complexidade espacial** é o quanto de memória adicional precisamos alocar no nosso algoritmo.

## Principais Classificações de Big O
Na ordem da que melhor para a que pior escala.

### O(1) ou constante
Independente do tamanho do input, o algoritmo sempre tem o mesmo tempo de execução.

Tempo: Encontrar o primeiro elemento de um array.

Memória: Encontrar os 15 maiores elementos de um array. Se esse número não mudar com o tamanho do input é O(1).

### O(log n)
Conforme o input aumenta rápido, o nosso tempo de execução ou memória não aumenta tão rápido.

Exemplos dessa escala logaritmica:
```
log₂(10) -> 3.321928
log₂(20) -> 4.321928
log₂(40) -> 5.321928
```
A entrada dobra e o tempo de execução/memória aumenta em 1.

Quando o input aumenta exponencialmente, o resultado aumenta linearmente.

Busca binária (binary search) escala em O(log n).

### O(n)
Escala na mesma medida que o input aumenta.

Tempo: quando percorremos todos os elementos de um array.

Memória: quando eu duplico o array do input ou retorno um array de mesmo tamanho do array original.
Ex. recebo `[1,2,3,4,5]` e preciso retornar `[2,4,6,8,10]`

### O(n log n)
Escala de forma linear X logarítmica, conforme o input dobra, o tempo de execução é um pouco mais que o dobro.

Algoritmos de sorting, como quicksort ou mergesort, têm essa complexidade, exceto o bubblesort, que é O(n²).

Algoritmos com essa complexidade percorrem todo um array, dividindo em subarrays de forma recursiva, mas não o suficiente para ser O(n²).

Percorre um array O(n) por O(log n) vezes.

Tempo: Algoritmos de sorting ou de 'dividir e conquistar'.

Memória: muito raro de existir. Merge sort tem memória O(n) e quicksort tem memória O(log n).

### O(n²)
Escala de forma quadrática

Algoritmos de loop dentro de um loop têm essa complexidade temporal.

O bubblesort tem essa complexidade.

Exemplos de memória quadrática:
Quando o input é um array e o output é um grafo ou matriz.

Ou recebo um array e preciso retornar todos os pares.
Ex. recebo `[1,2,3,4,5]` e preciso retornar `[[1,1],[1,2],[1,3],[1,4],[1,5],[2,1],[2,2][2,3],[2,4],[2,5]...]`

### Outros casos específicos que também existem
* **O(sqrt(n)) ou Complexidade Raiz Quadrada**
    * **Posição:** Entre O(log n) e O(n) (é mais rápido que linear).
    * **Exemplo:** Verificar se um número é primo (testando divisores apenas até a raiz quadrada de n).

* **O(2^n) ou Complexidade Exponencial**
    * **Posição:** Depois de O(n^2) (é muito mais lento).
    * **Exemplo:** Um algoritmo recursivo de Fibonacci.

* **O(n!) ou Complexidade Fatorial**
    * **Posição:** Depois de O(2^n) (uma das piores complexidades).
    * **Exemplo:** Resolver o "Problema do Caixeiro Viajante" com força bruta, testando todas as rotas (permutações) possíveis.


O(2^n) ou complexidade exponencial -> depois da O(n^2) -> algoritmo recursivo de fibonacci 

O(raiz de n) ou complexidade raiz quadratica -> entre O(log n) e O(n) -> ex de algoritmo, verifica se um numero é primo

O(n!) ou complexidade fatorial -> depois de o(2^n) -> ex de algorimo, resolver o problema do caixeiro viajante com brute force, testando todas as rotas possiveis
