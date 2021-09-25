#!/bin/bash

# Given an web user access log file, find the most frequent callers 
# 1.2.3.4 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" tel:200 2326


def getLogs():
    with open("logs") as logs:
        access = logs.readlines()
    return access

def printLogs(list_logs):
    for logs in list_logs:
        print(logs.strip().split(" ")[6])

def getMostAccess(list_logs):
    for logs in list_logs:
         pass




list_logs = getLogs()

printLogs(list_logs)


    
