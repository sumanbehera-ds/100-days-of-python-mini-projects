def remove_negative_numbers(numbers):
    result = []

    for number in numbers:
        if number >= 0:
            result.append(number)

    return result


values = [10, -5, 20, -2, 0, 8]

cleaned = remove_negative_numbers(values)

print("Original:", values)
print("Without negatives:", cleaned)