def sum_odd_numbers(numbers):
    total = 0

    for number in numbers:
        if number % 2 != 0:
            total += number

    return total


values = [1, 2, 3, 4, 5, 6, 7, 8]

answer = sum_odd_numbers(values)

print("List:", values)
print("Sum of odd numbers:", answer)