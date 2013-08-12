#temperature conversion prorgam
def celsius_to_fahrenheit(celsius_float):
    return celsius_float * 1.8 + 32
print("Convert Celsius to Fahrenheit.")
celsius_float = float(input("Enter a temperature in Celsius: "))
fahrenheit_float = celsius_to_fahrenheit(celsius_float)
print(celsius_float," converts to ", fahrenheit_float," Fahrenheit")
