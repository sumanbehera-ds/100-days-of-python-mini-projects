def intersection_lists(list1, list2):
    result = []

    for item in list1:
        if item in list2 and item not in result:
            result.append(item)

    return result


a = [1, 2, 3, 4, 5]

b = [3, 4, 5, 6, 7]

answer = intersection_lists(a, b)

print("Intersection:", answer)