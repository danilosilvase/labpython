# import json

# class Students:    
    
#     def get_students(self):
#         students = {
#             "001": {"name": "Bob", "class": "1A"},
#             "002": {"name": "Alice", "class": "1A"}
#         }

#         students["003"] = {
#             "name": "Ives",
#             "class": "1A"
#         }
#         return students         
    
#     def read_file(self, filename):
#         with open(filename) as infile:
#             # dict_json = {}
#             dict_json = json.load(infile)
#             return dict_json
            
#     def write_file(self, filename):
#         with open(filename, "w") as outfile:
#             students_parsed = json.dumps(self.get_students())
#             outfile.write(students_parsed)
            
#     def print_students(self):
#         [print("{} is studying in the class {}".format(value["name"],value["class"])) for code, value in self.get_students().items()]            

# def main():
#     students = Students()
#     students.write_file("students.json")
#     students.print_students()
#     students.read_file("students.json")
    
# if __name__ =="__main__":
#     main()

# import random

# def randons():
#     lista = [1, 5, 8, 2, 6]
#     print(random.randint(0,10))

#     random.shuffle(lista)
#     print(lista )

# randons()

# import random
# import dis

# def fibonacci(number):
#     if number == 1 or number == 0:
#         return 1
#     else:
#         return fibonacci(number - 1) + fibonacci(number - 2)

# def print_fibonacci():
#     calculed_list = map(fibonacci, range(0,10))
#     print((calculed_list))

# def main():
#     # dis.dis(fibonacci)
#     # print_fibonacci()
#     # num = 0
#     # function = lambda num: num + random.randint(0,10)
#     # print(function(5))
#     print((lambda x, y: x * y)(5, 6))

# if __name__ == "__main__":
#     main()

from collections import Counter

class ApacheLogs:

    def __init__(self, logfile):
        self.logfile = logfile
        
    def read_logs(self):
        with open(self.logfile) as infile:
            return Counter(tuple(line.strip().split(" ")[0] for line in infile)).most_common()
            
    def print_logs(self):        
        tuple(print("IP: {} => {}".format(ip, count)) for ip, count in self.read_logs())

def main():
    apache_logs = ApacheLogs("/Users/danlsil/workspace/Python/labpython/study/printWords/src/logs")
    apache_logs.print_logs()

if __name__ =="__main__":
    main()




    
