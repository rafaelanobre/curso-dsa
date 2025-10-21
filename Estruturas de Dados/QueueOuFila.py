from queue import Queue
from collections import deque

q = Queue()
# Métodos principais: put(), get(), empty(), qsize()

print(q.empty()) # True

q.put(1)
q.put(2)
q.put(3)

print(q.get())  # 1
print(q.get())  # 2

print("Size:", q.qsize())  # 1
print(q.empty())  # False