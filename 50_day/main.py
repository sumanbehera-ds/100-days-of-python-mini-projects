# Swap Two Numbers Without Third Variable
def swap_numbers(a, b):
    print("Before swap:")
    print("a =", a)
    print("b =", b)

    a = a + b
    b = a - b
    a = a - b

    print("After swap:")
    print("a =", a)
    print("b =", b)

    return a, b


swap_numbers(10, 20)