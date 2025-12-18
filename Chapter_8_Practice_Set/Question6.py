# Write a python function which converts inches to cms.

def inches_to_cms(inches):
    cma=inches*2.54
    return cma

inches=float(input("Enter length in inches: "))
print(f"{inches} inches is equal to {inches_to_cms(inches)} cms")
