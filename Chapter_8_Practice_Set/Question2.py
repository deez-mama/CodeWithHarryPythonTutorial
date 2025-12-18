# program using function to convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius * 9/5) + 32
    return fahrenheit

celsius=float(input("Enter temperature in Celsius: "))
print(f"{celsius} degree Celsius is equal to {celsius_to_fahrenheit(celsius)} degree Fahrenheit")
