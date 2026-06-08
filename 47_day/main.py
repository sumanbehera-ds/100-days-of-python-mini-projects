# Count Digits in a Number
def count_digits(number):
    number = abs(number)

    if number == 0:
        return 1

    count = 0

    while number > 0:
        count += 1
        number = number // 10

    return count


num = 987654

print("Number:", num)
print("Digits:", count_digits(num))