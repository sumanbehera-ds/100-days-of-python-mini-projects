def is_prime(number):
    if number <= 1:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def primes_in_range(start, end):
    primes = []

    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)

    return primes


print(primes_in_range(10, 50))