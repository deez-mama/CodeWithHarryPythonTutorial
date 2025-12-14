marks={
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    0 : "Harry"
}

print(marks.items())  # This will print all key-value pairs as tuples in a list
print(marks.keys())   # This will print all the keys in the dictionary
print(marks.values()) # This will print all the values in the dictionary

marks.update({"Bob": 95, "Ram" : 80})  # Updating Bob's marks
print(marks)

print(marks.get("Alice2"))  # This will return None since "Alice2" is not a key in the dictionary
print(marks("Alice2"))  # This will raise an error since dict is not callable