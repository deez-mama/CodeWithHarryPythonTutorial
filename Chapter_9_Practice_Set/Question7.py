# Write a program to find out the line number where python is present from ques 6.



with open("log.txt")as f:
    i=1
    while (i>0):
        line=f.readline().lower()
        if line != "":
            if "python" in line:
                print(f"Python is in line {i}")
                i+=1
            else:
                i+=1
        else:
            i=0