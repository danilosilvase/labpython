# You're given an application log file that contain the strings DEBUG, INFO, WARN, ERROR, CRITICAL.
# Find only the ERROR and CRITICAL lines

cat error.log | grep [ERROR|CRITICAL]

# Given an web user access log file, find the most frequent callers 
# 1.2.3.4 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" tel:200 2326

visits = {}
with open('logs') as file:
   for line in file:
       ip = file.split(' ')[0]
       visits[ip] = visits.get(ip, 0) + 1
sorted_visits = sorted(visits, key= lambda x in x: x[1])
print(sorted_visits[0])

    # Write a program that can read fortune files and returns a random fortune to the user.
    # Fortune Format Example: Fortunes are separated by a % sign on a single line followed by a newline character.
# This is a fortune
# %
# Here is
# Another fortune
# %
# What does the fox say?
# %
# The
# Cow%
# Says %
# Moo
fortunes = """^^"""
list_of_fortunes = fortunes.split('%')
random_number = random(0, len(list_fortunes))
print(list_of_fortunes[random_number])
list_of_fortunes = []
current_fortune = ""
for line in fortunes:
   if(line == '%'):
       list_of_fortunes.append(current_fortune)
   else:
       current_fortune += line
       
list_of_fortunes += current_fortune

Empty string
String thats just blank lines
Test%
%
%
%
This is fortune %
This is a thing%
hi%
-------

class Fortunes:
   __init__():
       self.count = 0
   
   def add_fortune(self,fortune):
       self.count += 1
       with open('fortune-self.count'):
               write(fortune)
               
   def get_random_fortune(self):
       random_fortune_id = random(0, self.count)
       with open(fortune-$random_fortune_id) as fortune_chunk:
           print(fortune_chunk)
   
   
fortunes = Fortunes()
current_fortune = ""
with open('input') as file
   for line in file:
       if(line == '%'):
           fortunes.add_fortune(current_fortune)
       else:
           current_fortune += line
   
   
fortunes.add_fortune(current_fortune)
print(fortunes.get_random_fortune())

# Write a function that takes an array as a parameter.
# The array contains non-negative numbers.
# Every number in the array appears an even number of times,
# except for one number that appears an odd number of times.
# The function should return the number that appears an odd number of times.
# Example: [1, 1, 5, 5, 2, 2, 2, 3, 3] => 2
# 1, 1 appears twice so even
# 2, 2, 2 appears three times so odd
# even is divisible by 2
count_of_digits = {} # 2
prev_digit = -1

for digit in input:
   if(digit != prev_digit) and count_of_digits[prev_digit]):
       break
       
   if(count_of_digits[input] is None)
       count_of_digits[input] = 1
   else:
       del count_of_digits[input]
       
   prev_digit = digit
       
print(count_of_digits)


Example: [1, 1, 1, 1, 3, 5, 5, 2, 2, 2, 3, 3, 3] => 2
2 3 4 5 6 7 8 9 10 J Q K A

# Hearts Diamonds Spades Clubs
# Hello darkness my old friend

class Card():
   def __init__(self, card):
       self.suite = card.suite
       self.number = card.number
   
   def get_number_for_letter(self, letter):
       letter_values = {
           'J': 11,
           'Q': 12,
           'K': 13,
           'A': 14
       }