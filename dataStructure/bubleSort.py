#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    numberOfSwaps = 0
    # Write your code here
    for element in range(0, n-1):
        for elements in range(0, n-1):
            if a[elements] > a[elements + 1]:
                a[elements], a[elements + 1] = a[elements +1], a[elements]
                numberOfSwaps += 1
           
        
print("Array is sorted in {} swaps.".format(numberOfSwaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))