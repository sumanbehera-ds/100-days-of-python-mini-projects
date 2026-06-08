# Create Multiplication Table
def multiplication_table(number):
    table = []

    for i in range(1, 11):
        result = number * i
        row = f"{number} x {i} = {result}"
        table.append(row)

    return table


num = 7

for line in multiplication_table(num):
    print(line)