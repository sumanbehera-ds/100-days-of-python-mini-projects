# Find Missing Number
def find_missing_number(numbers, n):
    expected_sum = n * (n + 1) // 2

    actual_sum = 0

    for num in numbers:
        actual_sum += num

    missing = expected_sum - actual_sum

    return missing


values = [1, 2, 4, 5, 6]

print("Missing number:", find_missing_number(values, 6))