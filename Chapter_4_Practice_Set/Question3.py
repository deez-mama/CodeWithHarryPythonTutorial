#Check that a tuple type cannot be changed in python.

my_tuple = (1, 2, 3, 4, 5)

my_tuple[0] = 10  # This will raise a TypeError because tuples are immutable
