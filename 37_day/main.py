# Find GCD of Two Numbers
def find_gcd(a, b):
    a = abs(a)
    b = abs(b)

    while b != 0:
        remainder = a % b

        a = b
        b = remainder

    return a


num1 = 48
num2 = 18

print("GCD:", find_gcd(num1, num2))