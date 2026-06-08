# Sort a List in Descending Order
def descending_sort(numbers):
    arr = numbers.copy()

    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


values = [10, 5, 30, 25, 15]

answer = descending_sort(values)

print("Original:", values)
print("Descending:", answer)