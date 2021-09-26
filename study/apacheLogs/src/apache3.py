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
        ips = [ip.strip().split(" ")[0] for ip in self.logs]  ## O(n)
        ip_frequent_access = (Counter(ips).most_common(4))
        # print(type(ip_frequent_access)) # this will return a list
        for ip, count in ip_frequent_access:
            print("{one} => {two}".format(one=ip, two=count))
              
def main():
    ap1 = ApacheParse()
    ap1.read_logs("/Users/danlsil/workspace/Python/labpython/study/apacheLogs/src/access_log")
    ap1.print_frequent_acess()

if __name__ == "__main__":
    main()
