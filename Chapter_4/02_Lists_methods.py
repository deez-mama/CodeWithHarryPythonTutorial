friend=["Apple","Orange",5,67.67,True,"Ram"]

friend.append("Banana") #adds at the end

print(friend)

# changes through the methods changes the list 
# unlike strings where the original string remains unchanged and every method creates a new string

#friend.sort() #sorts the list in ascending order BUT int and str cannot be compared so this doesn't work here
print(friend)
friend.reverse() #reverses the list
print(friend)
friend.remove(5) #removes the first occurrence of the value
print(friend)
print(friend.pop()) #removes the last element
print(friend)
