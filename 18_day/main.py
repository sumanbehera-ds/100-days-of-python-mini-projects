# ind Factorial
def factorial(n):
    if n < 0:
        return "Factorial not possible"

    result = 1

    for number in range(1, n + 1):
        result = result * number

    return result


num = 5
answer = factorial(num)

print("Number:", num)
print("Factorial:", answer)