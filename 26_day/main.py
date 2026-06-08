# Find Second Largest Number
def second_largest(numbers):
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return None

    unique_numbers.sort(reverse=True)

    second = unique_numbers[1]

    return second


values = [10, 30, 20, 30, 40, 40]

answer = second_largest(values)

print("List:", values)
print("Second largest:", answer)