# Find Sum of List Elements
def sum_list(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


values = [10, 20, 30, 40, 50]

answer = sum_list(values)

print("List:", values)
print("Sum:", answer)