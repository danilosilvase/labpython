#!/bin/bash

import os.path

class Customer:
    def __init__(self, c='', f='', l=''):
        self.c = c
        self.f = f
        self.l = l

    def fullName(self):
        return self.firtName + " " + self.lastName

def getCustomers():
    customers = {
        "a": Customer("a", "James", "Barker"),
        "b": Customer("b", "Jonathan", "D"),
        "c": Customer("c", "Aleem", "Janmohamed"),
        "d": Customer("d", "Ivo", "Galic"),
        "e": Customer("e", "Joel", "Griffiths"),
        "f": Customer("f", "Michael", "Spinks"),
        "g": Customer("g", "Victor", "Savkov"),
        "h": Customer("h", "Marcel", "Dempers")
      }
    return customers

def getCustomer(customerID):
    customers = getCustomers()
    return customers[customerID]

# ## Check if file exist
# if os.path.isfile("customers.log"):
#     print("file exists")
# else:
#     print("file does not erxist")

# # Open file
# f = open("customers.log")

# #Read and print file
# for customer in f:
#     print(customer)
# f.close()

# # Create file if it does not exist

# customers = getCustomers()
# for customerID in customers:
#     c = customers[customerID]
#     f.write(c.customerID + "," + c.firstName + c.lastName )



    