# Find LCM of Two Numbers
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def find_lcm(a, b):
    if a == 0 or b == 0:
        return 0

    gcd = find_gcd(a, b)

    lcm = abs(a * b) // gcd

    return lcm


print("LCM:", find_lcm(12, 18))