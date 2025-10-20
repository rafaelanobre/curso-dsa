# Array
Representado como um espaço contínuo na memória, é uma espécie de lista, que pode ser interpretado como tendo vários elementos.

Em algumas linguagens, como JavaScript, um array pode armazenar elementos de tipos diferentes.

Em outras mais de baixo nível, como Rust, todos os elementos do array devem ser do mesmo tipo.

## Entendendo memória, bytes e bits
Para entender arrays, precisamos entender como a memória do computador funciona.

A memória RAM do computador é composta de milhares de endereços, cada endereço armazena 1 byte (8 bits).

Cada endereço tem um identificador único, então a leitura e escrita é feita de forma muito rápida, acessando diretamente o endereço.

A memória é organizada em bytes, onde cada byte é composto por 8 bits.

Um bit pode ter valor 0 ou 1.
Um byte pode representar valores 256 valores diferentes, de 0 a 255.

Como ler binário é difícil, usamos a representação hexadecimal, onde cada dígito representa 4 bits (um nibble).
Por exemplo, o byte `11111111` em binário é `FF` em hexadecimal (15 * 16 + 15 = 255 em decimal).


## JavaScript Array
Isso não é um Array:

```javascript
let a = []
```

Mesmo sendo chamado de array em JavaScript, isso na verdade é um objeto muito mais complexo e com muito mais propriedades do que um array no sentido tradicional e low-level.

O 'array' do JavaScript usa arrays esparsos e perde a eficiência de memória e performance que um array tradicional teria.

O JavaScript moderno (ES6+) possui uma implementação próxima do conceito tradicional, chamada ArrayBuffer e os Typed Arrays (como Uint8Array), que são usados tanto no Node.js quanto nos navegadores."

```javascript
const a = new ArrayBuffer(8) // aloca 8 bytes contínuos na memória (64 bits)

const a8 = new Uint8Array(a) // interpreta o ArrayBuffer como um array de 8 bytes (8 bits cada)

a8 // Uint8Array(8) [ 0, 0, 0, 0, 0, 0, 0, 0 ]

const a32 = new Uint32Array(a) // interpreta o mesmo ArrayBuffer como um array de 2 inteiros de 32 bits (4 bytes cada)

a32 // Uint32Array(2) [ 0, 0 ]

a32[0] = 4294967295 // maior valor possível em um Uint32

a32 // Uint32Array(2) [ 4294967295, 0 ]

a // ArrayBuffer(8) { [Uint8Contents]: <ff ff ff ff 00 00 00 00>, byteLength: 8 }

a8 // Uint8Array(8) [ 255, 255, 255, 255, 0, 0, 0, 0 ]
```

O ArrayBuffer é o objeto que representa o bloco contínuo de memória (o "array tradicional").

Os TypedArray (como Uint8Array, Int32Array, Float64Array, etc.) são as "visões" que nos permitem ler e escrever nesse bloco de memória interpretando os bytes de formas diferentes.

## Python Array
O Python não causa essa confusão, pois o que normalmente é usado é chamado de lista (list).

A lista do Python não é um array tradicional, é um array de ponteiros, que na verdade é dinâmico.

Essa lista é um bloco contínuo de memória que armazena ponteiros para objetos alocados em outros endereços da memória.

Isso é flexível, mas requer mais memória e é menos eficiente do que um array tradicional, pois precisamos guardar o ponteiro e o objeto em si e o processador precisa fazer mais operações para acessar o valor real.

```python
lista = [1, "a", True] # Isso não armazena os valores juntos na memória.

# Na memória, se parece com isto:

# lista: [ (endereço 5040), (endereço 8010), (endereço 2030) ]

# Em algum lugar da memória...
# Endereço 5040: (o objeto número 1)
# Endereço 8010: (o objeto string "a")
# Endereço 2030: (o objeto booleano True)
```

Se quisermos um array tradicional em Python, podemos usar o módulo array da biblioteca padrão, que é mais próximo do conceito tradicional.

```python
import array as arr

array_real = arr.array('i', [10, 20, 30]) # I significa que todos os elementos são inteiros, geralmente ocupando 4 bytes cada.

# Na memória, isso É um bloco contínuo:
print(array_real) # array('i', [10, 20, 30])

# Em bytes (hexadecimal, 4 bytes por número):
# <0a 00 00 00 14 00 00 00 1e 00 00 00>
#    (número 10)  (número 20)  (número 30)
```

Eficiente em memória e muito rápido, pois os dados estão todos juntos (bom para o cache do processador).

Mais rígido. Não pode misturar tipos.

No módulo array, não usamos tipos do Python, mas valores que correspondem a tipos de dados básicos do C, usando typecodes na criação do array, como 'i', 'f' ou 'd'.

