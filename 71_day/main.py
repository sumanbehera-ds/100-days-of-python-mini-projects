# Count Frequency of Each Element in List
def frequency_count(items):
    frequency = {}

    for item in items:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

    return frequency


data = [1, 2, 2, 3, 3, 3, 4]

result = frequency_count(data)

print(result)