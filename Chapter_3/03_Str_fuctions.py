a="Bishowjeet"

print(a.endswith("jeet"))  # Output: True
print(a.endswith("jee"))  # Output: False
print(a.startswith("bis"))  # Output: False
print(a.startswith("Bis"))  # Output: True

print(a.capitalize())  # Output: Bishowjeet
print(a.lower())  # Output: bishowjeet
print(a.upper())  # Output: BISHOWJEET
print(a.count("e"))  # Output: 2
print(a.replace("jee", "joon"))  # Output: Bishowjoonet
print(a.find("je"))  # Output: 3