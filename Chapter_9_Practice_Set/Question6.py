# Write a program to mine a log file and find out whether it contains ‘python’

with open("log.txt")as f:
    contains=f.read().lower()
    if "python" in contains:
        print("Yes, the log file contains 'python'")
    else:
        print("The log file doesn't contain 'python'")
