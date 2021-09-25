#!/bin/python3

def print_dict():
    students_age = {} 
    read_name = input("Insert the name: ")
    while read_name != "exit":
        read_age = input("Insert the age: ")
        students_age[read_name] = read_age
        # print(students_age)        
        for key, value in students_age.items():
            print(key, value)
        read_name = input("Isert the name: ")

def main():
    print_dict()

if __name__ == '__main__':
    main()


