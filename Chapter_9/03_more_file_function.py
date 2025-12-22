f=open("file.txt") #we are opening in read mode so we don't have to specify read mode

#lines=f.readlines()

#print(lines, type(lines))

""" 
line1=f.readline()
print(line1,type(line1))

line2=f.readline()
print(line2,type(line2))

line3=f.readline()
print(line3,type(line3))
"""

line=f.readline()

while(line!=""):
    print(line)
    line=f.readline()

f.close()