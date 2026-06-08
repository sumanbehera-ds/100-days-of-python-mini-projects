# Sort a List in Ascending Order (Bubble Sort)
def bubble_sort(numbers):
    arr = numbers.copy()

    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


values = [64, 34, 25, 12, 22, 11, 90]

result = bubble_sort(values)

print("Original:", values)
print("Sorted:", result)