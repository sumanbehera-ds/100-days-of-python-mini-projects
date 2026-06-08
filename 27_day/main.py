# Check Armstrong Number
def is_armstrong(number):
    digits = str(number)

    power = len(digits)

    total = 0

    for digit in digits:
        total += int(digit) ** power

    if total == number:
        return True

    return False


num = 153

print("Number:", num)
print("Armstrong:", is_armstrong(num))