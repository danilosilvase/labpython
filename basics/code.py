##The array contains non-negative numbers.
##Every number in the array appears an even number of times, except for one number that appears an odd number of times.
##The function should return the number that appears an odd number of times.
## mod % 2 == 1 odd

##Example:
##[1, 1, 5, 5, 2, 2, 2, 3, 3, 1, 1] => 2

##[1, 1, 1, 1, 2, 2, 2, 3, 3, 5, 5] => 2

def find_odd3(input_list):
    input_list.sort()
    current = 0
    count = 1
    for index, number in enumerate(input_list):
        if number == input_list[index + 1]:
            count += 1
            current = number
        elif count % 2 == 1:
            return current        
        else:
            count = 1     
        
    

def find_odd(input_list):
    return [tuple(number for number in set(input_list) if input_list.count(number) % 2 == 1)[0]
    
    
def find_odd2(input_list):
    return tuple(tuple(number for number in set(input_list) if input_list.count(number) % 2 == 1)[0]
    


