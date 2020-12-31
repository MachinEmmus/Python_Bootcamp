#!/usr/bin/python3
"""Create a Double Matriz"""

matriz = [[], [], [], [], [], [], [], [], [], [], [], []]
for i in range(12):
    for j in range(12):
        if i % 2 == 0:
            j+=2
        matriz[i].append(i * j)
print(matriz)
