# Sum of Digits
def sum_of_digits(number):
    number = abs(number)

    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10

    return total


num = 12345
print("Number:", num)
print("Sum of digits:", sum_of_digits(num))