#!/bin/python3

# Given an web user access log file, find the most frequent callers 
# 1.2.3.4 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" tel:200 2326

from collections import Counter

class ApacheParse():
    
    def __init__(self):
        self.logs = []

    def read_logs(self, log_file: str) -> list:
        with open(log_file) as apache_logs:
            self.logs = apache_logs.readlines()
        
    def print_frequent_acess(self):
        ips = []
        for line in self.logs:
            ips.append(line.strip().split(" ")[0])
        ip_frequent_access = (Counter(ips)) # Counter will return a collection Couter, like a dictionary
        print(ip_frequent_access.most_common(5))

              
def main():
    ap1 = ApacheParse()
    ap1.read_logs("/Users/danlsil/workspace/Python/labpython/study/apacheLogs/src/access_log")
    ap1.print_frequent_acess()

if __name__ == "__main__":
    main()
