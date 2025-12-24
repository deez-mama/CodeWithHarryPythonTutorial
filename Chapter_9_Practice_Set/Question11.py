# Write a python program to rename a file to “renamed_by_ python.txt.


import os



with open("Filetorename.txt")as f: #reading the content of the file
    content=f.read()

with open("renamed_by_ python.txt","w")as f: #wrote the content to a new file
    f.write(content)

os.remove("Filetorename.txt") #deleted the file