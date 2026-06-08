def factorial_recursive(number):
    if number < 0:
        return None

    if number == 0 or number == 1:
        return 1

    result = number * factorial_recursive(number - 1)

    return result


num = 6

answer = factorial_recursive(num)

print("Number:", num)
print("Factorial:", answer)