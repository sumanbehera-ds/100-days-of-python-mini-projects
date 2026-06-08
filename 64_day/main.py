def find_index(items, target):
    for index in range(len(items)):
        if items[index] == target:
            return index

    return -1


data = ["apple", "banana", "mango", "orange"]

target = "mango"

answer = find_index(data, target)

print("List:", data)
print("Target:", target)
print("Index:", answer)