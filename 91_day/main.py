# Fibonacci Using Recursion
def fibonacci_recursive(number):
    if number < 0:
        return None

    if number == 0:
        return 0

    if number == 1:
        return 1

    return fibonacci_recursive(number - 1) + fibonacci_recursive(number - 2)


limit = 8

for i in range(limit):
    print(fibonacci_recursive(i))