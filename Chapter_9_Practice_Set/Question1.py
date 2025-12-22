# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

with open("poems.txt") as f:
    line=f.readline()
    while(line != ""):
        if "twinkle" in line:
            print("Yes! there is twinkle in the file.")
            exit()
        line=f.readline()


