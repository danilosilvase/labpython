#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = [[2, 1, 1, 0, 0, 2], [1, 1, 0, 0, 0, 1], [1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 2, 0], [1, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 3]]
    sum = 0
    for row in range(len(arr)):
        for col in range(6):
            sum += (arr[row][col])

    print(sum)










    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))
    # arr.extend([1, 1, 1, 0, 0, 0])
    # arr.extend([0, 1, 0, 0, 0, 0])
    # arr.extend([1, 1, 1, 0, 0, 0])
    # arr.extend([0, 0, 2, 4, 4, 0])
    # arr.extend([0, 0, 0, 2, 0, 0])
    # arr.extend([0, 0, 1, 2, 4, 0])

    # for j in range(0,4):
    #     for k in range(0,4):        
    #         sum = int(arr[j][k])
    #         # print(sum)
    # sum = 0
    # tarr = []
    
    # for l in range(0,4):
    #     for k in range(0,4):
    #         for i in range(l,l+3):
    #             for j in range(k,k+3):
    #                 if i == l+1 and ( j == k or j == k+2):
    #                     continue
    #                 else:
    #                     sum += arr[i][j]
    #         tarr.append(sum)
    #         sum = 0
    
    # print(max(tarr))
