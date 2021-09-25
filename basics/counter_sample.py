from collections import Counter
#define a list
list=[1,2,3,4,5,6,7,2,3,2,3]
#make instance of Counter
c=Counter(list)
print("list:",list,"\n")
print(c,"\n")

#define a tuple
tuple = ("apple", "banana", "cherry","orange","apple")
#make instance of Counter
c1=Counter(tuple)
print("\ntuple:",tuple,"\n")
print(c1,"\n")

#define a string
str="Python Programming" 
#make instance of Counter
c2=Counter(str)
print ("String:",str,"\n")
print(c2,"\n")

#define a dictionary
dict={'a':3,'b':2,'c':1}
#make instance of Counter
c3=Counter(dict)
print("Dictionary:",dict,"\n")
print(c3,"\n")