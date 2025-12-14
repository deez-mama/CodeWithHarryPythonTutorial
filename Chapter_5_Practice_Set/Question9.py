"""
Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}
"""

s = {8, 7, 12, "Harry", [1,2]}

print("No, we cannot change the values inside a list which is contained in set S because lists are mutable and sets require their elements to be immutable (hashable). Therefore, including a list inside a set will raise a TypeError.")
