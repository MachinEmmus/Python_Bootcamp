#!/usr/bin/python
num1 = input('Enter first integer numbers: ') 
num2 = input('Enter second integer numbers: ')

num1 = int(num1)
num2 = int(num2)

print("{:d} + {:d} = {:d}".format(num1, num2, (num1 + num2)))
print("{:d} - {:d} = {:d}".format(num1, num2, (num1 - num2)))
print("{:d} * {:d} = {:d}".format(num1, num2, (num1 * num2)))
print("{:d} / {:d} = {:d}".format(num1, num2, (num1 / num2)))
print("{:d} % {:d} = {:d}".format(num1, num2, (num1 % num2)))
