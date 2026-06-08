# Find Even and Odd Numbers
def split_even_odd(numbers):
    even_numbers = []
    odd_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return even_numbers, odd_numbers


values = [1, 2, 3, 4, 5, 6]

even, odd = split_even_odd(values)

print("Even:", even)
print("Odd:", odd)