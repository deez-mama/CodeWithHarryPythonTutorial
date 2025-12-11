#  Write a python program to print the contents of a directory using the os module.

import os

#Specify the directory path

directory_path='C:/Users/User/Desktop/Python/Chapter_1_PS'

#Get the list of all files and directories in the specified directory

contents=os.listdir(directory_path)

#Print each file and directory name

for items in contents:
    print(items)

