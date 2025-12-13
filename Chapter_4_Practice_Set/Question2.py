#Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

input1=int(input("Enter the marks of student 1: "))
marks.append(input1)
input2=int(input("Enter the marks of student 2: "))
marks.append(input2)
input3=int(input("Enter the marks of student 3: "))
marks.append(input3)
input4=int(input("Enter the marks of student 4: "))
marks.append(input4)
input5=int(input("Enter the marks of student 5: "))
marks.append(input5)
input6=int(input("Enter the marks of student 6: "))
marks.append(input6)
marks.sort()
print("The sorted marks of the students are: ")
print(marks)
