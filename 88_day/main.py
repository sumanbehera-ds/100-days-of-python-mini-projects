def is_prime(number):
    if number <= 1:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


def count_primes(numbers):
    count = 0

    for number in numbers:
        if is_prime(number):
            count += 1

    return count


values = [2, 3, 4, 5, 6, 7, 8, 9]

print("Prime count:", count_primes(values))