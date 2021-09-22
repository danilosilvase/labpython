#!/bin/bash

## Reading file log
def apache_log_reader(logfile):
    with open(logfile) as f:
        log = f.read()
    print(log)

if __name__ == '__main__':
    apache_log_reader("access_log")



 ## Data structure
 # 
 # 
 #    