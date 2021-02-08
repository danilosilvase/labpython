## Write me a python function that inputs a string and a list, then uses the list values to split the string into another list.

valueString = input("Please input the value string\n")

inputList = input("Please input the list, values may be separetd by spaces. Eg: value1 value2 vlaueN\n")

valueList = inputList.split(" ")

finalList = []

for name in valueList:
    if name == valueString:        
        finalList.append(list(name))
print(finalList)














#valueList2 = ["value1","value2","valuen"]

##print(valueString)

##print(*valueList)

##print(*valueList, sep = ", ")

##print(*valueList, sep = "\n")

##print(valueList[2])
#print(valueList2[2])

#print(' '.join(valueList))