## Apache logs

# from collections import Counter

# class ApacheLogs():
#     def __init__(self, logfile) -> None:
#         self.logfile = logfile
    
#     def read_logs(self) -> tuple:
#         with open(self.logfile) as access_logs:
#             print([line.strip().split(" ")[0] for line in access_logs])
            
#     # def print_access_logs(self) -> None:
#     #     [print("IP: {} => {}".format(ip, count)) for ip, count in self.read_logs()]
            
# def main():
#     apache_logs = ApacheLogs("/Users/danlsil/workspace/Python/labpython/study/printWords/src/logs")
#     # apache_logs.print_access_logs()
#     apache_logs.read_logs()
    
# if __name__ == "__main__":
#     main()




# Write a function that takes an array as a parameter.
# The array contains non-negative numbers.
# Every number in the array appears an even number of times,
# except for one number that appears an odd number of times.
# The function should return the number that appears an odd number of times.
# Example: [1, 1, 5, 5, 2, 2, 2, 3, 3] => 2

def find_odd_count(input_array) -> int:
    print(input_array.count(2))
    return [number for number in set(input_array) if input_array.count(number) % 2 == 1]
    
def main():
    input_array = [1, 1, 5, 5, 2, 2, 2, 3, 3]
    print(find_odd_count(input_array))
        
if __name__=="__main__":
    main()

# def find_odd_count(input_array) -> None:
#     print((number for number in input_array))
    
# def main():
#     input_array = [1, 1, 5, 5, 2, 2, 2, 3, 3]
#     find_odd_count(input_array)
        
# if __name__=="__main__":
#     print([0, 3 ,2][1])


# def print_students_lowest_grade(student_list):
#     grade_list = sorted([grade for student, grade in student_list])[:-2]
#     student_list.sort()        
#     [print("{}'s grade is {}.".format(student, grade)) for student, grade in student_list if grade in grade_list ]        
        
# def main():
#     student_list = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#     print_students_lowest_grade(student_list)

# if __name__=="__main__":
#     main()
    
    
# if __name__ == '__main__':
#     students = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         print(name)
#         print(score)
#         values = [name, score]
#         print(values)
#         students.append(values)

#     print(students)
        
#     grade_list = sorted([grade for student, grade in students])

#     students.sort()        
#     [print(student) for student, grade in students if grade in grade_list ] 


# if __name__ == '__main__':
#     students = []
#     n = int(input())
#     students = [[input(), float(input()) ] for _ in range(n)]
    
        
#     grade_list = sorted([grade for student, grade in students])[:-2]
#     students.sort()        
#     [print(student) for student, grade in students if grade in grade_list] 



# matrix = []

# for i in range(5):
	
# 	# Append an empty sublist inside the list
# 	matrix.append([])
	
# 	for j in range(5):
# 		matrix[i].append(j)
		
# print(matrix)


# print([[j for j in range(5)] for i in range(2)])

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# final_list = []
# for num_list in matrix:
#     final_list.extend(num_list)

# print(final_list)

# final_list = [var for sublist in matrix for var in sublist]
# print(final_list)

###### JSON

#### Json


# import json

# def read_json(jsonfile):
#     # jsonfile = '{"fruta": "laranja", "cor": "laranja", "sabor": "laranja"}'
#     with open(jsonfile) as jsonfiles:
#         dict_fruta = json.load(jsonfiles)
#     print(dict_fruta)
#     # return dict_fruta
    
# # def print_json(dict_fruta):
# #     print(dict_fruta)
#     # [print("{} => {}".format(key,value)) for key, value in dict_fruta.items()]


# # def write_json(dict_fruta):
# #     dict_fruta["famili"] = "laranja" 
# #     write_json = json.dumps(dict_fruta)

# #     with open("jsonfile", "w") as jsonwrite:
# #         jsonwrite.write(write_json)
    
# def main():
#     read_json("sample.json")
# #     write_json(read_json())
    
# if __name__=="__main__":
#     main()

# Python program to write JSON
# to a file
  
  
# import json
  
# # Data to be written
# dictionary ={
#     "name" : "sathiyajith",
#     "rollno" : 56,
#     "cgpa" : 8.6,
#     "phonenumber" : "9976770500"
# }
  
# # Serializing json 
# json_object = json.dumps(dictionary, indent = 4)
  
# # Writing to sample.json
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)


# import json
  
# # Opening JSON file
# with open('sample.json', 'r') as openfile:
  
#     # Reading from json file
#     json_object = json.load(openfile)
  
# print(json_object)
# print(type(json_object))



### JSON da massa

# import json

# class Students:
#     def __init__(self, jsonfile):
#         self.jsonfile = jsonfile

#     def read_json_file(self):
#         with open(self.jsonfile) as openfile:
#            students = json.load(openfile)
#         return students

#     def create_json_file(self):
#         students = {
#             "name": "Danilo",
#             "grade": "10",
#             "year": "2021",
#         }

#         #Searilizing the object
#         studens_json = json.dump(students, indent=4)
        
#         with open(self.jsonfile,"a") as writefile:
#             writefile.write(studens_json)
            
#     def print_json(self):       
#         [print("Key: {}, => Value: {}".format(key, value)) for key, value in self.read_json_file().items()]
        
        
# def main():
#     students = Students("students.json")
#     students.create_json_file()
#     students.print_json()
    
# if __name__ == "__main__":
#     main()



## Regular expression

# import re

# string = "O rato roeu a roupa do rei de roma"

# result = re.findall("[r..o]", string)
# print(result)

# result = re.sub("rato", "gato", string)
# print(result)


### CSV

# import csv
# from typing import Dict

# def write_csv(filename):
#     fruits = ["apple", "banana", "caju"]
#     rows = ["fruitA", "fruitB", "fruitC"]
#     with open(filename, "a") as fruitsfile:
#         # csv_file = Dict.Writer(fruits)
#         # fruitsfile.write(csv_file)
#         writer = csv.writer(fruitsfile)
#         writer.writerow(rows)
#         writer.writerow(fruits)


# def main():
#     write_csv("fruitsfile")

# if __name__=="__main__":
#     main()


# You're given an application log file that contain the strings DEBUG, INFO, WARN, ERROR, CRITICAL.
# Find only the ERROR and CRITICAL lines

# class Logs:
    
#     def read_logs(self, logfile):
#         with open(logfile) as logs:
#             return [line.strip() for line in logs if "ERROR" in line or "CRITICAL" in line]
            
#     def print_logs(self, filtered_list):
#        [print(line, sep="\n") for line in filtered_list]
    
# def main():
#     logs = Logs()
#     filtered_list = logs.read_logs("/Users/danlsil/workspace/Deployment/EKS/Review/logs.log")
#     logs.print_logs(filtered_list)
    
# if __name__ == "__main__":
#     main()

# Given an web user access log file, find the most frequent callers 
# 1.2.3.4 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" tel:200 2326

# from collections import Counter

# class WebLogs:
    
#     def __init__(self, logfile):
#         self.logfile = logfile
    
#     def read_file(self):
#         with open(self.logfile) as weblogs:
#             return Counter([line.strip().split(" ")[0] for line in weblogs]).most_common()
    
#     def print_frequent_callers(self):
#         [print("IP: {} => {}".format(ip, count)) for ip, count in self.read_file()]
        
    
# def main():
#     weblogs = WebLogs("/Users/danlsil/workspace/Python/labpython/study/printWords/src/logs")
#     weblogs.print_frequent_callers()

# if __name__ =="__main__":
#     main()


# def print_inverse_list(input_list):
#     print(input_list[::-1])
    
# def main():
#     input_list = [6, 7 ,4 ,1]
#     print_inverse_list(input_list)

# if __name__ == "__main__":
#     main()
    
# def join_strings(string_a, string_b):
#     return "".join((string_a, string_b))
    
# def main():
#     string_a = "ele"
#     string_b = "phante"
#     print(join_strings(string_a, string_b))
    
# if __name__ == "__main__":
#     main()
    
# def fibonacci(number):
#     if number == 0:
#         return 0
#     elif number == 1:
#         return 1
#     else:
#         return fibonacci(number - 1) + fibonacci(number - 2)
        
# def main():
#     [print(fibonacci(num)) for num in range(100,200)]
    
# if __name__ == "__main__":
#     main()

# def fibonacci(number):
#     if number == 0:
#         return 0
#     if number == 1:
#         return 1
#     else:
#         return fibonacci(number - 1) + fibonacci(number - 2)
        
# def main():
#     [print(fibonacci(num)) for num in range(1)]
    
# if __name__ == "__main__":
#     main()


##  word = 1s2e3n4h5a

# import json


# def extratc_numbers(word):
#     string = ""
#     result = ["".join((string + letter)) for letter in word if letter not in str(list(range(10)))]
#     print("".join(result))

   
# def main():
#     word = "1s2e3n4h5a"
#     extratc_numbers(word)
    
# if __name__=="__main__":
#     main()