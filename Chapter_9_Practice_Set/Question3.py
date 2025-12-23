# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.

for i in range (2,21):
    with open (f"Multiplication table {i}","w")as f:
        for n in range (1,11):
            product=n*i
            f.write(str(product))
            f.write(" ")

