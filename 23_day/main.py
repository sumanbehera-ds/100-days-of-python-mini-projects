# Remove Duplicates From List
def remove_duplicates(items):
    unique_items = []

    for item in items:
        if item not in unique_items:
            unique_items.append(item)

    return unique_items


numbers = [1, 2, 2, 3, 4, 4, 5]

result = remove_duplicates(numbers)

print("Original:", numbers)
print("Unique:", result)