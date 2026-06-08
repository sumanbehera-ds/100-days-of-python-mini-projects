def largest_even_number(numbers):
    largest = None

    for number in numbers:
        if number % 2 == 0:
            if largest is None or number > largest:
                largest = number

    return largest


values = [11, 24, 35, 48, 59, 62]

answer = largest_even_number(values)

print("List:", values)
print("Largest even:", answer)