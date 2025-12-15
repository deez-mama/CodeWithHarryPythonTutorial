"""
Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass.
Assume 3 subjects and take marks as an input from the user.
"""

subject1=int(input("Enter marks of subject 1:"))
subject2=int(input("Enter marks of subject 2:"))
subject3=int(input("Enter marks of subject 3:"))

total_marks=subject1+subject2+subject3
percentage=total_marks/3
if(percentage>=40 and subject1>=33 and subject2>=33 and subject3>=33):
    print("Congratulations! You have passed the exam.")
else:
    print("Unfortunately, you have failed the exam. ")
