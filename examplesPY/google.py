#!/usr/bin/python3
numbers = [1, 2, 4, 4]
sum = 8
for n in numbers:
    for m in numbers:
        if n + m == sum:
            print("True")
        else:
            print("False")
