# Merge Two Sorted Lists
def merge_sorted_lists(a, b):
    i = 0
    j = 0
    merged = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    merged.extend(a[i:])
    merged.extend(b[j:])

    return merged


print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))