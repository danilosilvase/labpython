#  Q: Write a function that takes an array of integers as an input and returns the length of the
#  longest consecutive sequence within. Example {5,17,1,19,3,24,2,16,4,32,15} >> longest sequence is 5
#  elements {1,2,3,4,5} so should return 5

N = [5,17,1,19,3,24,2,16,4,32,15,6,8,55,56,57,58,60,61,62,63,64,65,66,67]

N.sort()
count = 1
bigger = 0

for (index, item) in enumerate(N):
    last = (item-1)
    if last == (N[index-1]):
        count = count + 1
        if count > bigger:
            bigger = count
    else:
        count = 1
print(bigger)



