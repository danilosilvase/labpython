# You're given an application log file that contain the strings DEBUG, INFO, WARN, ERROR, CRITICAL.
# Find only the ERROR and CRITICAL lines

# class ReadLogs():

#     def read_and_print_file_log(self, logfile):
#         with open(logfile) as app_logs:
#             list_error_logs = tuple([line.strip() for line in app_logs if "ERROR" in line or "CRITICAL" in line])
#             print(*list_error_logs, sep="\n")
            
# def main():
#     get_logs = ReadLogs()
#     get_logs.read_and_print_file_log("/Users/danlsil/workspace/Deployment/EKS/Review/logs.log")
    
# if __name__ == "__main__":
#     main()


## Primes

# def print_primes_in_range(start: int, stop: int):
#     for number in range(start, stop):
#         if all([number % i != 0 for i in range(2,number)]):
#             print(number)

# def main():
#     print_primes_in_range(100,200)
    
# if __name__ == "__main__":
#     main()

### Fibonacci

# def fibonacci(input_value):
#     if input_value == 0:
#         return 0
#     if input_value == 1:
#         return 1
#     else:
#         return fibonacci(input_value - 1) + fibonacci(input_value -2)

# def main():
#     for num in range(2,10):
#         print(fibonacci(num))

# main()

# Given an web user access log file, find the most frequent callers 

# 1.2.3.4 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" tel:200 2326

# from collections import Counter

# class FilterLogs():
    
#     def __init__(self):
#         self.frequent_callers = ()

#     def read_log_file(self, logfile):
#         with open(logfile) as logs:
#             self.frequent_callers = Counter((line.strip().split(" ")[0] for line in logs)).most_common()
    
#     def print_frequent_callers(self):
#         for ip, count in self.frequent_callers[::-1]:
#             print("IP: {} => {}".format(ip, count))
            
# def main():
#     filter_logs = FilterLogs()
#     filter_logs.read_log_file("/Users/danlsil/workspace/Python/labpython/study/printWords/src/logs")
#     filter_logs.print_frequent_callers()
    
# if __name__ == "__main__":
#     main()
        
# import random

# class Fortune():
#     def __init__(self, user, fortune_file):
#         self.user = user
#         self.fortune_file = fortune_file

#     def read_fortune_file(self):
#         with open(self.fortune_file) as fortunes:
#             fortune = random.choice([line.strip().split("%") for line in fortunes][0])
#         return fortune
    
#     def assign_fortune(self):
#         print("{}'s fortune is {}".format(self.user, self.read_fortune_file()))
        
# def main():
#     fortune = Fortune("Danilo","/tmp/fortune")
#     fortune.assign_fortune()
    
# if __name__ == "__main__":
#     main()

# def find_odd_numbers(input_array):
#     print(*[number for number in set(input_array) if input_array.count(number) % 2 == 1])
    
# def main():
#     input_array = [1, 1, 5, 5, 2, 2, 2, 3, 3]
#     find_odd_numbers(input_array)

# if __name__ == '__main__':
#     main()

# from itertools import groupby

# def find_odd_numbers(input_array):
#     grouped_numbers = groupby(input_array)
#     for item, group in grouped_numbers:
#         if len(list(group)) % 2 == 1:
#             print(item)
            
# input_array =  [1, 1, 5, 5, 2, 2, 2, 3, 3]          
# find_odd_numbers(input_array)


# from itertools import groupby

# def find_odd_numbers(input_array):
#     grouped_list = ([list(number) for item, number in groupby(input_array)])
#     print(grouped_list)

#     print(*(number[0] for number in grouped_list if len(number) % 2 == 1))            

# input_array =  [1, 1, 5, 5, 2, 2, 2, 3, 3]          
# find_odd_numbers(input_array)


# from itertools import groupby

# def find_odd_numbers(input_array):
#     grouped_list = list(groupby(input_array))
#     print([number[0] for key, number in grouped_list])
            

# input_array =  [1, 1, 5, 5, 2, 2, 2, 3, 3]          
# find_odd_numbers(input_array)


# Write a function that takes an array as a parameter.
# The array contains non-negative numbers.
# Every number in the array appears an even number of times,
# except for one number that appears an odd number of times.
# The function should return the number that appears an odd number of times.
# Example: [1, 1, 5, 5, 2, 2, 2, 3, 3] => 2
# 1, 1 appears twice so even
# 2, 2, 2 appears three times so odd
# even is divisible by 2

# from collections import Counter
# from itertools import groupby

# def find_odd_count(input_array) -> int:
#     odd_numbers = Counter(input_array).most_common()
#     print(odd_numbers, sep="\n")
#     # odd_numbers2 = groupby(input_array)
#     print([num for num in [list(number) for key, number in groupby(input_array)] if len(num) % 2 ==1 ], sep="\n")


#     # odd = [number for number, count in Counter(input_array).values if count % 2 == 1]
#     # return odd[0]
    
        
# def main():
#     input_array = [1, 1, 5, 5, 2, 2, 2, 3, 3]
#     print(find_odd_count(input_array))
    
# if __name__== "__main__":
#     main()

# from itertools import groupby

### Using Groupby

# def find_odd_number(array):
#     # odd_numbers = [list(number_group) for key, number_group in groupby(array)]
#     numbers_list = [number for number in [list(number_group) for key, number_group in groupby(array)] if len(number) % 2 == 1]
#     print(numbers_list)
    
## Using Counter

# from collections import Counter

# def find_odd_number(array):
#     numbers_list = [num for num, count in Counter((num for num in array)).most_common() if count % 2 == 1]
#     print(numbers_list[0])


# # ### Using count

# def find_odd_number(array):
#     numbers_list = [array.count(num) for num in set(array) if array.count(num) % 2 == 1]
#     print(numbers_list)

# ### Using conventional loop

# def main():
#     array =  [1, 1, 5, 5, 2, 2, 2, 3, 3, 3]
#     find_odd_number(array)
    
# if __name__== "__main__":
#     main()



# def factorial(number):
#     if number < 2:
#         return 1
#     else:
#         return number * factorial(number - 1)
        
# def main():
#     input = 5
#     print(*[factorial(number) for number in range(1,5+1)] , sep="\n")
    
# if __name__ == "__main__":
#     main()


    
#### Fibonacci

# def fibonacci(number):
#     if number == 0:
#         return 0
#     if number == 1:
#         return 1
#     else:
#         return fibonacci(number - 1) + fibonacci(number - 2)
        
# def main():
#     print(*[fibonacci(item) for item in range(1, 25)], sep="\n")
    
# if __name__ == "__main__":
#     main()
    
#### Prime

### isPrime if { p > 1 and (p-1 > 1) % 2 != 0}
### print from x to y

# def prime(start, stop):
#     for number in range(start, stop):
#         if all([number % i != 0 for i in range(2, number)]):
#             print(number)
            
# def main():
#     prime(100, 200)
    
# if __name__ == "__main__":
#     main()