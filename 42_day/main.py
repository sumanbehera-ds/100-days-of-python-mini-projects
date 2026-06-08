# Find All Divisors of a Number
def find_divisors(number):
    divisors = []

    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)

    return divisors


num = 24

result = find_divisors(num)

print("Number:", num)
print("Divisors:", result)