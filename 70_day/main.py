# Find Duplicate Elements in a List
def find_duplicates(numbers):
    seen = set()

    duplicates = set()

    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)

    return list(duplicates)


values = [1, 2, 3, 2, 4, 5, 1, 6]

print(find_duplicates(values))