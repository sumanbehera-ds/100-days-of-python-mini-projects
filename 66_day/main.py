# Find Minimum Number in a List
def find_minimum(numbers):
    if len(numbers) == 0:
        return None

    minimum = numbers[0]

    for number in numbers:
        if number < minimum:
            minimum = number

    return minimum


values = [45, 12, 78, 3, 56, 89]

answer = find_minimum(values)

print("List:", values)
print("Minimum:", answer)