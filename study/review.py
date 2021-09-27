
# You're given an application log file that contain the strings DEBUG, INFO, WARN, ERROR, CRITICAL.
# Output: print lines -  Find only the ERROR and CRITICAL lines

# class ReadLogs():
#     def __init__(self):
#         self.logs = []

#     def read_log_file(self, logfile):
#         with open(logfile) as logs:
#             self.logs = [line.strip() for line in logs]
#             # for line in logs:
#             #     self.logs.append(line)
            
#     def print_logs(self):
#         print(*[line for line in self.logs if "ERROR" in line or "CRITICAL" in line], sep="\n")
#         # for line in self.logs:
#         #     if "ERROR" in line or "CRITICAL" in line:
#         #         print(line)

# def main():
#     read_logs = ReadLogs()
#     read_logs.read_log_file("/Users/danlsil/workspace/Deployment/EKS/Review/logs.log")
#     read_logs.print_logs()
    
# if __name__=="__main__":
#     main()


# from collections import Counter

# class ReadLogsApache():
#     def __init__(self):
#         self.logs = []
#         self.frequent_callers = []
        
#     def read_log_file(self, logfile):
#         with open(logfile) as logs:
#             self.logs = [line.strip().split(" ")[0] for line in logs]            
    
#     def find_frequent_callers(self):
#         self.frequent_callers = Counter(self.logs).most_common()
#         return self.frequent_callers
        
#     def print_frequent_caller(self):
#         print_list = self.find_frequent_callers()
#         for ip,count in print_list:
#             print("IP: {} => count: {}".format(ip, count))
            
# def main():
#     readlogs = ReadLogsApache()
#     readlogs.read_log_file("/Users/danlsil/workspace/Python/labpython/study/printWords/src/logs")
#     readlogs.print_frequent_caller()
    
# if __name__=="__main__":
#     main()

# Write a program that can read fortune files and returns a random fortune to the user.
# Fortune Format Example: Fortunes are separated by a % sign on a single line followed by a newline character.
# output #

# import random

# class Fortune():
#     def __init__(self, name):
#         self.name = name
#         self.ramdon_fortune = []
        
#     def read_fortune_files(self, fortunefile):
#         with open(fortunefile) as fortunes:
#             self.ramdon_fortune = [line.strip().split("%") for line in fortunes]
#         return(random.choice(self.ramdon_fortune[0]))
                    
#     def print_fortune(self):
#         print("The {}'s fortune is {}".format(self.name, self.read_fortune_files("/tmp/fortune")))
        
# def main():
#     user1 = Fortune("Danilo")
#     user1.print_fortune()
    
# if __name__ =="__main__":
#     main()
        
# Write a function that takes an array as a parameter.
# The array contains non-negative numbers.
# Every number in the array appears an even number of times,
# except for one number that appears an odd number of times.
# The function should return the number that appears an odd number of times.
# Example: [1, 1, 5, 5, 2, 2, 2, 3, 3] => 2
# 1, 1 appears twice so even
# 2, 2, 2 appears three times so odd
# even is divisible by 2


# def get_odd_number_times(list_numbers):
#     list_number_unique = set(list_numbers)
#     print(*[number for number in list_number_unique if list_numbers.count(number) % 2 == 1], sep="\n")    
    
# def main():
#     list_numbers = [1, 1, 5, 5, 2, 2, 2, 3, 3,66666]
#     get_odd_number_times(list_numbers)
    
# if __name__ =="__main__":
#     main()


# def sum_cards(list_cards):
#     sum_values = 0
#     cards = {
#         "J": 11,
#         "Q": 12,
#         "K": 13,
#         "A": 14
#     }
#     for card in list_cards:
#         if card in range(1,11):
#             sum_values += card
#         else:
#             sum_values += cards[card]        
#     print(sum_values)
        
# def main():
#     list_cards = [1, 6, 8, 9,"J", "K", "A"]
#     sum_cards(list_cards)
    
# if __name__=="__main__":
#     main()
            
# class Prime():
    
#     def print_prime(self, start: int, stop: int):
#         for number in range(start, stop):
#             if all(number % i != 0 for i in range(2, number)):
#                 print(number)

# def main():
#     prime = Prime()
#     prime.print_prime(100, 200)

# if __name__=="__main__":
#     main()


## Fibonnaci

# def fibonacci(n: int):
#     if n < 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n - 2)
        
# def print_fibonacci(start: int, stop: int):
#     for num in range(start,stop):
#         print(fibonacci(num))
        
# def main():
#     print_fibonacci(1, 10)
    
# if __name__ =="__main__":
#     main()
    
## Factorial
## !n whre n = 0 or n = 1 equals 1

# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n - 1)
        
# def main():
#     print(factorial(50))
    
# if __name__=="__main__":
#     main()
    