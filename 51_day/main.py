# Find Average of Numbers
def find_average(numbers):
    if len(numbers) == 0:
        return 0

    total = 0

    for number in numbers:
        total += number

    average = total / len(numbers)

    return average


values = [10, 20, 30, 40]

print("Average:", find_average(values))