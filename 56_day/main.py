# Find Cube of List Elements
def cube_elements(numbers):
    cubes = []

    for number in numbers:
        cube = number ** 3
        cubes.append(cube)

    return cubes


values = [1, 2, 3, 4, 5]

result = cube_elements(values)

print("Original:", values)
print("Cubes:", result)