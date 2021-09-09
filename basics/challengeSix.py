#!/usr/bin/env python3

# Number of test cases
i = int(input().strip())

# List of caracters

for loop in range(i):

    s = list(input().strip())

    s1 = []
    s2 = []

    separator = ""

    for (index, item) in enumerate(s):
       # print(s.index(item))
        if index % 2 == 0:
            s1.append(item)
        else:
            s2.append(item)

    print(separator.join(map(str,s1)) +' '+separator.join(map(str,s2))) 



