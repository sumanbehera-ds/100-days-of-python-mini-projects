# Check Perfect Number
def is_perfect_number(number):
    if number <= 0:
        return False

    total = 0

    for i in range(1, number):
        if number % i == 0:
            total += i

    return total == number


num = 28

print("Number:", num)
print("Perfect number:", is_perfect_number(num))