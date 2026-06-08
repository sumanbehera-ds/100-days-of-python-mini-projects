# Find Largest Number in List
def find_largest(numbers):
    if len(numbers) == 0:
        return None

    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


values = [10, 45, 3, 99, 23]

print("List:", values)
print("Largest:", find_largest(values))