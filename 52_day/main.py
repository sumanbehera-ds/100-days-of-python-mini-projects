# Count Positive and Negative Numbers
def count_positive_negative(numbers):
    positive = 0
    negative = 0
    zero = 0

    for number in numbers:
        if number > 0:
            positive += 1
        elif number < 0:
            negative += 1
        else:
            zero += 1

    return positive, negative, zero


values = [1, -2, 3, 0, -5, 6]

print(count_positive_negative(values))