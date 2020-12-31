#!/usr/bin/python3
""" Implement List Comprehension """
pares = []
for num in range(31):
    if num % 2 == 0:
        pares.append(num)
"""---Without List Comprehension---"""
print(pares)
"""---List Comprehension---"""
print("even = [num for num in range(31) if num % 2 == 0]")
even = [num for num in range(31) if num % 2 == 0]
print(even)

""" Implement Dict Comprehension """
dicty = {}
for num in range(11):
    dicty[num] = num**2
"""---Without Dictyonary Comprehension---"""
print(dicty)
"""---Dictyonary Comprehension---"""
print("dicto = {num : num**2 for num in range(11)}")
emmus = {num: num**2 for num in range(11)}
print(emmus)
