# Find Pair With Given Sum
def find_pair_with_sum(numbers, target):
    seen = set()

    for number in numbers:
        needed = target - number

        if needed in seen:
            return needed, number

        seen.add(number)

    return None


values = [2, 7, 11, 15]

target_sum = 9

print(find_pair_with_sum(values, target_sum))