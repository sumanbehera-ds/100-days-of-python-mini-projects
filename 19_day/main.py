# Fibonacci Series
def fibonacci_series(limit):
    first = 0
    second = 1

    series = []

    for i in range(limit):
        series.append(first)

        next_number = first + second

        first = second
        second = next_number

    return series


print(fibonacci_series(10))