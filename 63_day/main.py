def convert_to_integers(items):
    numbers = []

    for item in items:
        number = int(item)
        numbers.append(number)

    return numbers


string_numbers = ["10", "20", "30", "40"]

result = convert_to_integers(string_numbers)

print("Original:", string_numbers)
print("Converted:", result)