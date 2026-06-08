def product_of_list(numbers):
    if len(numbers) == 0:
        return 0

    product = 1

    for number in numbers:
        product *= number

    return product


values = [2, 3, 4, 5]

answer = product_of_list(values)

print("List:", values)
print("Product:", answer)