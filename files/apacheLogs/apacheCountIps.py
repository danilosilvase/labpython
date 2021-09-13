import re
from collections import Counter

def apache_log_reader(logfile):
    myregex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    with open(logfile) as f:
        log = f.read()
        myiplist = re.findall(myregex, log)
        ipCount = Counter(myiplist)
        for k, v in ipCount.items():
            print("IP Address" +  " => " + str(k) + " " + "Count" + " => " + str(v) )

# Create entry point of our code

if __name__ == '__main__':
    apache_log_reader("access_log")

