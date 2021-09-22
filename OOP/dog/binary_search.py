class Numbers():

    # Binary search receive as input a list and a item and return the position
    def searchNumbers(self, list, item):
        low = 0
        high = len(list)-1
        while low <= high:
            midle = (low + high) // 2
            guess = list[midle]         
            if guess == item:
                return 2
            if guess < item:
               low = midle + 1
            else:
                high = midle - 1
        return None            

    def printNumbers(self, number):
        if number is not None:
            print("The number is at the position {}".format(number))
        else:
            print("Number not found")

## Execution

lista = [1, 3, 4, 6, 7, 8, 9]
number = 4
newNumber = Numbers()
result = newNumber.searchNumbers(lista, number)
newNumber.printNumbers(result)

## Performance
## Run time: O(log n) - Linear time



    



        





