# showing different data structures for a list of items
arr = [1,2, 'a', 4]

for i in arr:
    print(i)

import array as arr
# bytearray: 8 zeroed mutable bytes
b = bytearray(8)
print(b)            # bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00')

# array: typed unsigned bytes
a = arr.array('B', [0]*8)
print(a)            # array('B', [0, 0, 0, 0, 0, 0, 0, 0])

# memoryview: view into the bytearray (no copy)
mv = memoryview(b)
mv[0] = 255
print(b)            # bytearray(b'\xff\x00\x00\x00\x00\x00\x00\x00')

import array as arr

array_real = arr.array('i', [10, 20, 30]) # I significa que todos os elementos são inteiros, geralmente ocupando 4 bytes cada.

# Na memória, isso É um bloco contínuo:
print(array_real) # array('i', [10, 20, 30])

# Em bytes (hexadecimal, 4 bytes por número):
# <0a 00 00 00 14 00 00 00 1e 00 00 00>
#    (número 10)  (número 20)  (número 30)