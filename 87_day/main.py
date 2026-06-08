def largest_odd_number(numbers):
    largest = None

    for number in numbers:
        if number % 2 != 0:
            if largest is None or number > largest:
                largest = number

    return largest


values = [10, 21, 34, 45, 56, 67]

answer = largest_odd_number(values)

print("List:", values)
print("Largest odd:", answer)