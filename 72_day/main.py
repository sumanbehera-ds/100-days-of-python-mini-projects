# Rotate List Left by One Position
def rotate_left(numbers):
    if len(numbers) == 0:
        return numbers

    first = numbers[0]

    rotated = numbers[1:]

    rotated.append(first)

    return rotated


values = [10, 20, 30, 40, 50]

print(rotate_left(values))