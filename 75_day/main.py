# Find Difference Between Two Lists
def list_difference(list1, list2):
    result = []

    for item in list1:
        if item not in list2:
            result.append(item)

    return result


a = [1, 2, 3, 4, 5]

b = [2, 4]

answer = list_difference(a, b)

print(answer)