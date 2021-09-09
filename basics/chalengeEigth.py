
n = int(input())

dic = dict(input().split() for x in range(n))

names = []

while True:
    try:
        compare = str(input())
        if compare:
            names.append(compare)         
    except:
        break
 
for x in names:
    if dic.get(x) != None:
        phone = dic[x]
        print(x+"="+phone)
    else:
        print("Not found")

