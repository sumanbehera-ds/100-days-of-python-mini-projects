# Linear Search
def linear_search(items, target):
    index = 0

    while index < len(items):
        if items[index] == target:
            return index

        index += 1

    return -1


data = ["red", "green", "blue", "yellow"]

target = "blue"

print("Index:", linear_search(data, target))