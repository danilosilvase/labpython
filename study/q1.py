# Write a function that takes an array as a parameter.
# The array contains non-negative numbers.
# Every number in the array appears an even number of times, except for one number that appears an odd number of times.
# The function should return the number that appears an odd number of times.
# Example 1: [1, 1, 2, 2, 2, 3, 3, 5, 5] => 2
# Example 2: [1, 1, 2, 2, 2, 2, 2, 3, 3, 5, 5] => 2

from itertools import groupby

N = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]

lista = ([list(j) for i, j in groupby(N)])

for itens in lista:
    if len(itens) % 2 == 1:
        print(itens[0])