# Rotate List Right by One Position
def rotate_right(numbers):
    if len(numbers) == 0:
        return numbers

    last = numbers[-1]

    rotated = [last]

    rotated.extend(numbers[:-1])

    return rotated


values = [10, 20, 30, 40, 50]

print(rotate_right(values))