# Write a program to find out whether a file is identical & matches the content of another file.

with open ("this.txt")as f:
    content1=f.read()

with open ("Copyofthis.txt")as f:
    content2=f.read()

if content1==content2:
    print("The contents of the two file match")
else:
    print("The content of the two files aren't exactly same")