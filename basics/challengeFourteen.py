class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        #diff = self.__elements[0] - self.__elements[1]
        
        
        diff = max(self.__elements) - min(self.__elements)
        
        
        #if diff < 0:
        #    diff = diff * (-1)
        self.maximumDifference = diff
        
   
        
    
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)