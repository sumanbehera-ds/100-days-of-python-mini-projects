# Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32

    return fahrenheit


temperature_c = 37

temperature_f = celsius_to_fahrenheit(temperature_c)

print("Celsius:", temperature_c)

print("Fahrenheit:", temperature_f)