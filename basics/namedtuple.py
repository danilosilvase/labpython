# Python2

from collections import namedtuple
n = int(input())
headers = raw_input()
student = namedtuple('Student',headers)
students = []
for i in range(n):
    students.append(student(*raw_input().split()))
print sum(list(map(lambda x: float(x.MARKS),students)))/len(students)




# Python3

from collections import namedtuple
N, headers, total = int(input()), list(input().split()), 0
for _ in range(N):
    total += int(list(input().split())[headers.index('MARKS')])
print(total/N)
