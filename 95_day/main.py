# Move Zeros to End
def move_zeros_to_end(numbers):
    result = []

    zero_count = 0

    for number in numbers:
        if number == 0:
            zero_count += 1
        else:
            result.append(number)

    for i in range(zero_count):
        result.append(0)

    return result


values = [0, 1, 0, 3, 12]

print(move_zeros_to_end(values))