#!/bin/python3

# Given an web user access log file, find the most frequent callers 
# 1.2.3.4 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" tel:200 2326

from collections import Counter



def readFiles(logfile):
    callers = []
    with open(logfile) as file:
        for logs in file:
            # print(logs)
            callers.append(logs.strip().split(" ")[0])
        maxValues = dict(Counter(callers))
        print(maxValues)
 



        


    
if __name__ == "__main__":
    readFiles("/Users/danlsil/workspace/Python/labpython/study/apacheLogs/src/access_log")
