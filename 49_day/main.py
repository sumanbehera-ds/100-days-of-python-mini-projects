# Check Palindrome Number
def is_palindrome_number(number):
    original = number

    reversed_num = 0

    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number = number // 10

    return original == reversed_num


num = 121

print("Number:", num)
print("Palindrome:", is_palindrome_number(num))