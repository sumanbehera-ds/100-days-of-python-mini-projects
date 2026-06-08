# Find Numbers Divisible by 3 and 5
def divisible_by_3_and_5(start, end):
    result = []

    for number in range(start, end + 1):
        if number % 3 == 0 and number % 5 == 0:
            result.append(number)

    return result


start_value = 1
end_value = 100

answer = divisible_by_3_and_5(start_value, end_value)

print(answer)