# Find Union of Two Lists
def union_lists(list1, list2):
    result = []

    for item in list1:
        if item not in result:
            result.append(item)

    for item in list2:
        if item not in result:
            result.append(item)

    return result


a = [1, 2, 3, 4]

b = [3, 4, 5, 6]

print(union_lists(a, b))