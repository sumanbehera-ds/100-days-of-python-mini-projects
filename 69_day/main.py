# Check if List is Sorted
def is_sorted(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False

    return True


values = [1, 2, 3, 4, 5]

result = is_sorted(values)

print("List:", values)
print("Sorted:", result)