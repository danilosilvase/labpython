
# You're given an application log file that contain the strings DEBUG, INFO, WARN, ERROR, CRITICAL.
# Find only the ERROR and CRITICAL lines


def read_file_logs(logfile):
    with open(logfile) as logs:
        for line in logs:
            if "ERROR" in line or "CRITICAL" in line:
                print(line)
                
def main():
    read_file_logs("/Users/danlsil/workspace/Python/labpython/study/printWords/src/logs")
    
if __name__== "__main__":
    main()
        