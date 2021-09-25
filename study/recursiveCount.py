#!/bin/python3

# write a code to sum all values in a array using recursion

import random

def quick_sort(array):
    
    if len(array) < 2:
        return array
    else:
        pivolt = array[0]
        less = [item for item in array[1:] if item <= pivolt]
        greater = [item for item in array[1:] if item > pivolt]
        return quick_sort(less) + [pivolt] + quick_sort(greater)

def main():
    result = quick_sort([11, 2 ,6, 7, 8, 4, 10])
    print(result)

if __name__ == '__main__':
    main()

