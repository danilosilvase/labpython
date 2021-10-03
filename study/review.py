
# You're given an application log file that contain the strings DEBUG, INFO, WARN, ERROR, CRITICAL.
# Output: print lines -  Find only the ERROR and CRITICAL lines

class ReadLogs():
    def __init__(self):
        self.logs = []

    def read_log_file(self, logfile):
        with open(logfile) as logs:
            self.logs = [line.strip() for line in logs]
            # for line in logs:
            #     self.logs.append(line)
            
    def print_logs(self):
        print(*[line for line in self.logs if "ERROR" in line or "CRITICAL" in line], sep="\n")
        # for line in self.logs:
        #     if "ERROR" in line or "CRITICAL" in line:
        #         print(line)

def main():
    read_logs = ReadLogs()
    read_logs.read_log_file("/Users/danlsil/workspace/Deployment/EKS/Review/logs.log")
    read_logs.print_logs()
    
if __name__=="__main__":
    main()


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


# Write a function that takes an array as a parameter.
# The array contains non-negative numbers.
# Every number in the array appears an even number of times,
# except for one number that appears an odd number of times.
# The function should return the number that appears an odd number of times.
# Example: [1, 1, 5, 5, 2, 2, 2, 3, 3] => 2

def find_odd_count(input_array) -> int:
    return [number for number in set(input_array) if input_array.count(number) % 2 == 1][0]
    
def main():
    input_array = [1, 1, 5, 5, 2, 2, 2, 3, 3]
    print(find_odd_count(input_array))
        
if __name__=="__main__":
    main()

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

# 2. Write a Sort function to sort the elements in a list 

# def sort_list(list):
#     list.sort()
#     print(list)
    
# def main():
#     list = [55, 67, 32, 98, 23, 76, 43, 99, 2, 1]
#     sort_list(list)
    
# if __name__=="__main__":
#     main()


# Write a sorting function without using the list.sort function

# Write a sorting function without using the list.sort function

# output ==>> serted list

# def quick_sort(array_list: list) -> list:
#     if len(array_list) < 2:
#         return array_list
#     else:
#         pivolt = array_list[0]
#         left = [num for num in array_list[1::] if num <= pivolt]
#         right = [num for num in array_list[1::] if num > pivolt]
#         return quick_sort(left) + [pivolt] + quick_sort(right)
        
# def main():
#     list = [55, 67, 32, 98, 23, 76, 43, 99, 2, 1]
#     print(quick_sort(list))

# if __name__=="__main__":
#     main()


# Write a Python program to print a list in reverse

# def print_reverse(input_list):
#     output_list = input_list[::-1]
#     print(output_list)

# def main():
#     list = [55, 67, 32, 98, 23, 76, 43, 99, 2, 1]
#     print_reverse(list)
    
# if __name__=="__main__":
#     main()


# Write a Python program to check whether a string is a Palindrome or not 
# Output: is palindrome| is not palindrome

# class Palindrome():
    
#     def check_palindrome(self, input_istring: str):
#         if input_istring == input_istring[::-1]:
#             return True
#         else:
#             return False 
                    
# def main():
#     is_palindrome = Palindrome()
#     input_string = input()
#     while input_string != "exit":
#         if is_palindrome.check_palindrome(input_string):
#             print("is palindrome")
#         else:
#             print("is not palindrome")
#         input_string = input()
        
# if __name__=="__main__":
#     main()

# class PrintDuplicate():
    
#     # def print_duplicates(self, input_list):
#     #     for number in set(input_list):
#     #         if input_list.count(number) > 1:
#     #             print(number)

#     def print_duplicates(self, input_list):
#         print(set([x for x in input_list if input_list.count(x) > 1 ]))

                
# def main():
#     print_duplicate = PrintDuplicate()
#     input = [111, 222, 44444, 666, 7, 9, 5, 222, 9, 555, 555, 111]
#     print_duplicate.print_duplicates(input)
    
# if __name__=="__main__":
#     main()


### Input = [111, 222, 44444, 666, 7, 9, 5, 222, 9, 111]
# output = [111, 222, 9]

# class PrintDuplicate():
    
#     def print_duplicates(self, input_list):
#         for number in set(input_list):        
#             if input_list.count(number) > 1:
#                 print(number)
                
# def main():
#     print_duplicate = PrintDuplicate()
#     input = [111, 222, 44444, 666, 7, 9, 5, 222, 9, 111]
#     print_duplicate.print_duplicates(input)
    
# if __name__=="__main__":
#     main()


# class NumberWords():
#     def print_number_words(self, input_sentence):
#         list_words = input_sentence.strip().split(" ")
#         print(len(list_words))
        
# def main():
#     sentence = "O rato roeu a roupa do rei de roma"
#     app = NumberWords()
#     app.print_number_words(sentence)
    
# if __name__== "__main__":
#     main()


# def search_element_in_array(array, element):
#     if element in array:
#         print("Element found!")
#     else:
#         print("Element not found!")
        
# def main():
#     array = [111, 222, 44444, 666, 7, 9, 5, 222, 9, 111]
#     search_element_in_array(array, 5)
    
# if __name__== "__main__":
#     main()


## Write a Python program to implement a Binary Search 

# class BinarySearch():

#     def search(self, array, element):
#         low = 0
#         high = len(array) - 1
#         while low <= high:
#             midle = (low + high) // 2
#             guess = array[midle]
#             if guess == element:
#                 return midle
#             if element >= array[midle]:
#                 low = midle + 1
#             else:
#                 high = midle - 1
#         return None
        
# def main():
#     array = [111, 222, 44444, 666, 7, 9, 5, 222, 9, 111, 51]
#     array2 = list(set(array))
#     array2.sort()
#     print(array2)
#     binary = BinarySearch()
#     result = binary.search(array2, 51)
#     if result is None:
#         print("Elemend does not exist")
#     else:
#         print("The element is on the index {}".format(result))
    
# if __name__ =="__main__":
#     main()


### Write a Python program to join two strings

# def join_strings(string1, string2):
#     print("".join((string1,string2)))
    
# def main():
#     string1 = "abc"
#     string2 = "123"
#     join_strings(string1, string2)
    
# if __name__== "__main__":
#     main()
        
## Given a string as your input, delete any reoccurring character, and return the new string.

# def delete_recurrent(string):
#     newstring = set(string)
#     print("".join(newstring))
    
# def main():
#     string = "arara"
#     delete_recurrent(string)

# if __name__ == "__main__":
#     main()
    
## Write a Python program to extract digits from given string 

# class ExtracDigits():
#     def extratc(self, string, digit):
#         for index, letter in enumerate(string):
#             if letter == digit:
#                 list(string).pop(index)
#         print(string)
        
# class main():
#     ext = ExtracDigits()
#     ext.extratc("arara","r")
    
# if __name__ == "__main__":
#     main()
                
 