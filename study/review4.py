
## 15. Given a string as your input, delete any reoccurring character, and return the new string.

# def remove_reocurring_char(string: str):
#     new_string = ""
#     aux_list = []
#     for char in string:
#         if char not in aux_list:
#             aux_list.append(char)
#             new_string += char
#     return(new_string)
    
# def main():
#     string = "passaro"
#     print(remove_reocurring_char(string))
    
# if __name__=="__main__":
#     main()
    
## 14. Write a Python program to split strings using newline delimiter 

# def split_strings(input_phrase):
#     splited_words =  input_phrase.strip().split(" ")
#     print(*splited_words, sep="\n")
    
# def main():
#     input_phrase = ("O rato roeu a roupa do rei de roma")
#     split_strings(input_phrase)
    
# if __name__ == "__main__":
#     main()

## 13. Write a Python program to extract digits from given string 
#### s1t2r3i4n5g6
### 123456

# class ExtractDigits:
    
#     def check_digits(self, input_string): 
#         list_digits = str(list(range(10)))
#         result = [char for char in input_string if char not in list_digits]
#         return "".join(result)
        
# def main():
#     extract_digits = ExtractDigits()
#     input_string = "s1t2r3i4n5g6999"
#     print(extract_digits.check_digits(input_string))
    
# if __name__ == "__main__":
#     main()
               
## 12. Write a Python program to join two strings (Hint: using join()) 

# def join_strings(string_a, string_b):
#     return "".join((string_a, string_b))
    
# def main():
#     string_a = "can"
#     string_b = "guru"    
#     print(join_strings(string_a, string_b))
    
# if __name__ == "__main__":
#     main()


# 10. Write a Python program to implement a Binary Search 
# given an array and a number, return the index number in array

# def binary_search(array, number):
#     min = 0
#     max = len(array) - 1
#     while min <= max:
#         midle = (min + max) // 2
#         guess = array[midle]
#         if guess == number:
#             return midle
#         if number < guess:
#             max = midle - 1
#         else:
#             min = midle + 1
            
# def main():
#     number = 6
#     array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     print(binary_search(array, number))
    
# if __name__ == "__main__":
#     main()


## Given an array arr[] of n elements, write a Python function to search a given element x in arr[]. 
### 

# def search_element(array, element):
#     if element in array:
#         return "Element found"
#     else:
#         return "Element not found"
        
# def main():
#     array = [1, 3, 5, 6, 9]
#     element = 3
#     print(search_element(array, element))
    
# if __name__ =="__main__":
#     main()
    
### 8. Write a Python program to print number of words in a given sentence 

# def get_number_words(sentence: str) -> int:
#     return len(sentence.strip().split(" "))
    
# def main():
#     sentence = "o rato roeu a roupa do rei de roma"
#     print(get_number_words(sentence))
    
# if __name__ == "__main__":
#     main()
    

## 7. Write a Python program to print set of duplicates in a list 
#### list = [2, 2, 2, 3, 4, 5, 5, 7, 7, 9]
### 5, 7


# def print_duplicates(input_list):        
#     [print(item) for item in set(input_list) if input_list.count(item) == 2]

# def main():
#     input_list = [2, 2, 2, 3, 4, 5, 5, 7, 7, 9]
#     print_duplicates(input_list)
    
# if __name__ == "__main__":
#     main()
    

### 6. Write a Python program to check whether a string is a Palindrome or not 

# class Palindrome:
    
#     def is_palindrome(self, string: str):
#         if string == string[::-1]:
#             print("Is a palindrome")
#         else:
#             print("Is not a palindrome")

# def main():
#     palindrome = Palindrome()
#     palindrome.is_palindrome("ararad")
    
# if __name__ == "__main__":
#     main()

# #### 5. Write a Python program to print a list in reverse 

# def print_reverse(input_list):
#     print(input_list[::-1])
    
# def main():
#     input_list = [2, 2, 2, 3, 4, 5, 5, 7, 7, 9]
#     print_reverse(input_list)
    
# if __name__ =="__main__":
#     main()

## 4. Write a Python program to print Fibonacci Series 

# class Fibonacci:
    
#     def fibonacci(self, position):
#         self.position = position
#         if self.position == 0:
#             return 0
#         elif self.position == 1:
#             return 1
#         else:
#             return self.fibonacci(position - 1) + self.fibonacci(position - 2)
            
# def main():
#     fibonacci = Fibonacci()
#     print([fibonacci.fibonacci(position) for position in range(10)])
    
# if __name__ == "__main__":
#     main()

#### 3. Write a sorting function without using the list.sort function 

#### 3. Write a sorting function without using the list.sort function 

# def quick_sort(input_list):
#     if len(input_list) < 2:
#         return input_list
#     else:
#         pivolt = input_list[0]
#         left = [number for number in input_list[1::] if number <= pivolt]
#         right = [number for number in input_list[1::] if number > pivolt]
#         return quick_sort(left) + [pivolt] + quick_sort(right)
        
# def main():
#     array = [76, 37, 23, 45, 34, 37, 56, 23, 54, 64]
#     print(quick_sort(array))
    
# if __name__ =="__main__":
#     main()


### 2. Write a Sort function to sort the elements in a list 

# def sort_elements(input_list):    
#     return sorted(input_list)


# def main():
#     array = [76, 37, 23, 45, 34, 37, 56, 23, 54, 64]
#     print(sort_elements(array))
    
# if __name__=="__main__":
#     main()


### 1. Write a Python Program to print Prime Numbers between 2 numbers 
### prime is an int for all p > 1 and p only / by p.
### 30 to 40

    
### 1. Write a Python Program to print Prime Numbers between 2 numbers 
### prime is an int for all p > 1 and p only / by p.
### 30 to 40

### 1. Write a Python Program to print Prime Numbers between 2 numbers 
### prime is an int for all p > 1 and p only / by p.
### 30 to 40

# class Prime:
    
#     def find_primes(self, start, stop):
#         for number in range(start, stop):
#             if all([number % i != 0 for i in range(2, number)]):
#                 print(number)
                
# def main():
#     prime = Prime()
#     prime.find_primes(100, 200)
    
# if __name__ =="__main__":
#     main()
        
# class Prime:
    
#     def find_primes(self, start, stop):            
#         primes = [number for number in range(start, stop) if all([number % i != 0 for i in range(2, number)]) ]
#         print(primes)
                
# def main():
#     prime = Prime()
#     prime.find_primes(100, 200)
    
# if __name__ =="__main__":
#     main()
        
              

### Factorial

# def factorial(number):
#     if number == 0 or number == 1:
#         return 1
#     else:
#         return number * factorial(number - 1)
        
# def main():
#     number = 5
#     print(factorial(number))
    
# if __name__ == "__main__":
#     main()
        

### radom

# import random

# def generate_random():
#     # print("sample 1: {}".format(random(1,9)))
#     print("sample 2: {}".format(random.choice(range(9))))
#     option2 = random.choice(range(9))
#     LOGFILE = "ARQUIVO"
#     logfile = "".join((LOGFILE,str(option2)))

#     with open(logfile) as infile:
#         pass

# def main():
#     generate_random()

# if __name__=="__main__":
#     main()

import random

class Fortune:
    
    def read_fortune(self, fortunefile):
        with open(fortunefile) as infile:
            fortunes = infile.readline().strip().split("%")
            print(type(fortunes))
            return random.choice(fortunes)
            
    def assign_fortune(self, user_name: str,fortune_value: str):
        print("{}'s fortune is ${}".format(user_name, fortune_value))

def main():
    fortune = Fortune()
    fortune_value = fortune.read_fortune("/tmp/fortune")
    fortune.assign_fortune("Bob", fortune_value)
    
if __name__ == "__main__":
    main()




