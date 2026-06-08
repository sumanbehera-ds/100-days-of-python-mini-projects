def count_occurrence(items, target):
    count = 0

    for item in items:
        if item == target:
            count += 1

    return count


data = [1, 2, 3, 2, 4, 2, 5]

target = 2

print("Occurrence:", count_occurrence(data, target))