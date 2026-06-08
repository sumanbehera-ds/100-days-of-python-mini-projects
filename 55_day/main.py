# Find Squares of List Elements
def square_elements(numbers):
    squares = []

    for number in numbers:
        square = number ** 2
        squares.append(square)

    return squares


values = [1, 2, 3, 4, 5]

result = square_elements(values)

print("Original:", values)
print("Squares:", result)